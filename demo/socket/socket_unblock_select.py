#coding:utf8
from socket import *
import select



socket_server = socket(AF_INET, SOCK_STREAM)
socket_server.bind(("", 7788))
socket_server.listen(5)

socket_lists = [socket_server]

while True:
    """ 
    (linux/unix)操作系统提供了一个select接口，轮询给定的文件描述符状态，返回有变化的文件描述符
    存在文件描述符限制，即操作系统允许打开最大文件数量存在限制
    """
    """
    select(rlist, wlist, xlist[, timeout])
    在此只监听读的状态，程序阻塞在这，不消耗CPU，如果列表里面的值读状态变化后，就解阻塞
    """
    read_lists, _, _ = select.select(socket_lists, [], [])
    print(read_lists)
    for sock in read_lists:
        
        if sock == socket_server:
            # 新连接
            new_socket, client_info = socket_server.accept()
            print("client: %s " % str(client_info))
            socket_lists.append(new_socket)
        else:
            # 不是主客户端，即接收消息
            raw_data = sock.recv(1024)
            if raw_data:
                print("recv: %s" % raw_data)
            else:
                # 如果没有数据，则客户端断开连接
                sock.close()
                socket_lists.remove(sock)
                
                
