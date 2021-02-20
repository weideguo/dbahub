#!/bin/env python
# -*- coding: utf-8 -*-
"""
实现任意两个端口转发
端口可以分为本地端口、远端端口
至少需要指定一个本地端口用于监听请求服务
指定的端口不分先后，可以多个进程叠加转发
支持python2.7 python3.7
python rtcp.py 172.16.2.150:22 8222        #通过连接本地端口8222，可以实现连接远端端口172.16.2.150:22
"""
import os
import sys
import time
import socket
import threading


streams = [None, None]  

def _usage():
    print( "usage:\npython rtcp.py stream1 stream2\n\nstream: port or host:port")


def _get_another_stream(num):
    """
    从streams获取另外一个流对象，如果当前为空，则等待
    """
    if num == 0:
        another_num = 1
    elif num == 1:
        another_num = 0
    else:
        raise Exception("ERROR")

    while streams[another_num] == None:
        print("%s waiting another stream" % num)
        time.sleep(1)
    print("%s get another stream success" % num)    
    return streams[another_num]
        
        
def _transfer_stream(num, s1, s2):
    """
    交换两个流的数据
    """
    try:
        while True:
            #recv函数会阻塞，直到对端完全关闭
            buff = s1.recv(1024)
            if len(buff) == 0: #对端关闭连接，读不到数据
                print(num,"closing...")
                break
            print(num,"recv")
            #print(buff)
            s2.sendall(buff)
            print(num,"resend")
    except :
        print(num,"error occur")

    #close后需要一定时间才能释放端口，因此使用shutdown
    try:
        s1.shutdown(socket.SHUT_RDWR)
        s1.close()
    except:
        pass

    try:
        s2.shutdown(socket.SHUT_RDWR)
        s2.close()
    except:
        pass

    streams[0] = None
    streams[1] = None
    print(num, "CLOSED")


def _server(port, num):
    """
    处理服务情况，num为流编号（第0号还是第1号）
    """
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(("0.0.0.0", port))
    print("%s listen port: %s" % (num,port))
    srv.listen(1)
    while True:
        conn, addr = srv.accept()
        print("%s connect from: %s:%i" % (num,addr[0],addr[1]))
        streams[num] = conn                      # 存储流对象
        s2 = _get_another_stream(num)            # 获取另一端流对象
        _transfer_stream(num, conn, s2)


def _connect(host, port, num):
    """   
    处理连接，num为流编号（第0号还是第1号）
    """
    not_connet_time = 1
    wait_time = 1
    try_cnt = 1
    while True:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            conn.connect((host, port))
        except Exception:
            print("%s can not connect %s:%s" % (num, host, port))
            not_connet_time += 1
            if not_connet_time > try_cnt:
                print("%s connect timeout %s:%s" % (num, host, port))          # 连接远端端口超时
                os._exit(1)                                                    # sys.exit只结束线程
            else:
                time.sleep(wait_time)
                continue

        print("%s connect to %s:%i" % (num, host, port))
        streams[num] = conn                        # 放入本端流对象
        s2 = _get_another_stream(num)              # 获取另一端流对象
        _transfer_stream(num, conn, s2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        _usage()
        sys.exit(1)
    tlist = []  
    targv = [ sys.argv[1], sys.argv[2] ]
    for i in [0, 1]:
        s = targv[i]         # stream描述 ip:port 或 port
        sl = s.split(":")
        if len(sl) == 1:     # port
            t = threading.Thread(target=_server, args=(int(sl[0]), i))
            tlist.append(t)
        elif len(sl) == 2 :  # host:port
            t = threading.Thread(target=_connect, args=(sl[0], int(sl[1]), i))
            tlist.append(t)
        else:
            _usage()
            sys.exit(1)

    for t in tlist:
        t.start()
    for t in tlist:
        t.join()
    sys.exit(0)
