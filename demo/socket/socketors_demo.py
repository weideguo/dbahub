# -*- coding: utf-8 -*- 
#!/bin/env python3

import selectors
import socket

"""
事件驱动
selectors模块中包含了select和epoll，会根据系统自动识别
select/poll/epoll不断的轮询所负责的所有socket，当某个socket有数据到达了，就通知用户进程
select/epoll的优势并不是对于单个连接能处理得更快，而是在于能处理更多的连接
"""


def _read(conn,mask):
    #print(conn,mask)
    data = conn.recv(1024)
    import time
    time.sleep(10)
    if data:
        print(data)
        conn.send(data)
    else:
        print("client close")
        sel.unregister(conn)
        conn.close()
        
#实际处理过程 根据实际需要开进程/线程/协程进行处理
def read(conn,mask):
    from threading import Thread
    t=Thread(target=_read,args=(conn,mask))
    t.start()



sel = selectors.DefaultSelector()
def accept(server,mask):
    conn,addr = server.accept()
    print("new conn ",addr)
    #print(conn)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)  #新连接注册read回调函数
    print("register done")



server = socket.socket()
server.bind(('127.0.0.1',9998))
server.listen()
server.setblocking(False)
sel.register(server,selectors.EVENT_READ,accept)


while True:
    print("wait new event")
    events = sel.select()                         #默认阻塞，有活动连接就返回活动的连接列表
    #print(events)
    for key,mask in events:
        #print(key,mask)
        callback = key.data                      
        #print("key.data:",key.data)
        #print("key.fileobj:",key.fileobj)
        callback(key.fileobj,mask)               
        
        
        
