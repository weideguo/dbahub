#coding:utf8
#广播信息不会被路由器转发 因而不能跨域

#sender
from socket import *
dest=('192.168.59.255',8000)                 #主机所在网段的广播地址 
s=socket(AF_INET,SOCK_DGRAM)                 #udp不是面向连接才有广播、组播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)      #设置广播
data='who am i'
s.sendto(data.encode(),dest)



#receiver
from socket import *
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind(('0.0.0.0',8000))                     #客户端与发送端应该处于同一网段
msg,addr=s.recvfrom(1024)                    #阻塞接受指定长度的消息