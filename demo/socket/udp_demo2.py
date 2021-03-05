#udp双向通信

#server
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',9911))

BUFFSIZE=1024

msg,addr=s.recvfrom(BUFFSIZE)                       
print(msg,addr)                                           
"""
利用addr可以与client通信，即使client通过nat转换
假设server处于公网，则addr为公网ip与端口，其他任意服务器可以通过addr穿透nat与client通信？
受限于NAT类型，锥型NAT可以打洞，对称型NAT不能
对称NAT是一个请求对应一个端口，非对称NAT是多个请求对应一个端口
"""

data="helloxxxx"

s.sendto(data.encode(),addr)








#client
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('',9912))

data="hello"

dest=('10.10.19.13',9911)                                 #服务端监听的ip 端口

s.sendto(data.encode(),dest)

print(s.recvfrom(1024))   