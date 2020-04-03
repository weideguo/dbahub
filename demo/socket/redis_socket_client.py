#coding:utf8
#只依赖socket实现的redis客户端demo
import socket

host, port = "127.0.0.1",6379
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(tuple([host, port]))
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)


#结尾必须为"\n"
c="auth my_redis_passwd\n"
c="set a aaa\n"
c="get a\n"
c="hmset a1 a aaa b bbb\n"
c="hgetall a1\n"
ret = sock.send(c)  
sock.recv(1024 * 8)

