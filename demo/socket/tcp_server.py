#!/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading
import time

def tcplink(sock,addr):
	print 'Accept new connection from %s:%s...' % addr
    	sock.send('Welcome!')
    	while True:
        	data=sock.recv(1024)
        	if data=='exit' or not data:
            		break
        	sock.send('Hello,%s'%data)
    	sock.close()
    	print 'Connection from %s:%s closed.'%addr


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.bind(('127.0.0.1',9911))
s.listen(5)
"""
it specifies the number of unaccepted connections that the system will allow before refusing new
    connections.
"""
print 'Waiting for connection...'

threads=[]
while True:   
   	sock,addr=s.accept() 
   	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()
	threads.append(t)

for t in threads:
	t.join()

print "all exit"





#######################################################################
socket([family[, type[, proto]]])

#family
"""
AF_UNIX, AF_LOCAL 本地通信
AF_INET   IPv4网络通信
AF_INET6  IPv6网络通信
AF_PACKET 链路层通信
"""

#对于AF_INET协议族
#type
#数据流包含了多个数据包
"""
SOCK_STREAM 流套接字       处理TCP
SOCK_DGRAM  数据包套接字   处理UDP
SOCK_RAW    原始套接字     处理ICMP、IGMP等网络报文 
"""

#决定使用哪种协议
#protocol
"""
操作系统内核中定义支持的protocol有一个特殊的值IPPROTO_IP(IPPROTO_IP为0)，可以理解为一个通配符或默认值，即不指定protocol，由内核自己决定使用哪一个protocol。
"""





