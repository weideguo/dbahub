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

#SOCK_STREAM TCP
#SOCK_DGRAM  UDP
#SOCK_RAW



s.bind(('127.0.0.1',9911))
s.listen(5)
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

