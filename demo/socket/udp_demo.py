#

#server
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',9911))

BUFSIZE=1024

print(s.recvfrom(BUFSIZE))                         
"""
阻塞直到获取数据 
BUFSIZE值必须大于sendto的长度，一次recvfrom与一次sendto对应，而不是像tcp可以迭代获取部分长度的消息
TCP是面向流的协议，而UDP是面向数据报的协议
"""







#client
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.bind(('192.168.253.128',9912))                     #客户端也可以绑定端口，如果绑定，则不随机分配一个端口

data="hello"

dest=('192.168.253.128',9911) 

s.sendto(data.encode(),dest)

#s.connect(dest)
#s.send(data.encode())

