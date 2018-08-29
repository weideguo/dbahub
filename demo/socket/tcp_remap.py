# -*- coding: utf-8 -*-
import socket
import threading
import time

def tcplink(sock,addr,to_host,to_port):
	print 'Accept new connection from %s:%s' % addr
    	while True:
        	data=sock.recv(4096)
		print data
        	if data=='exit' or not data:
            		break
		##remap to new ip:port
		sock_remap=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock_remap.connect((to_host,to_port))
		sock_remap.send(data)

		response=sock_remap.recv(4096)
        	sock.send(response)
		print str(data)
		print response
    	sock.close()
    	print 'Connection from %s:%s closed.'%addr


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9911))
s.listen(5)

to_host='127.0.0.1'
to_port=6381

print 'Waiting for connection...'

threads=[]
while True:
   
   	sock,addr=s.accept() 
   	t=threading.Thread(target=tcplink,args=(sock,addr,to_host,to_port))
	t.start()
	threads.append(t)

for t in threads:
	t.join()

print "all exit"
