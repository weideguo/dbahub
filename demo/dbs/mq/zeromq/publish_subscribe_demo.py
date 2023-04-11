#广播订阅模式


import zmq 

context = zmq.Context()  
socket = context.socket(zmq.PUB)  
socket.bind("tcp://127.0.0.1:5000") 
 
msg = "publish message"
#广播消息给订阅者 没有阻塞
socket.send(msg)               
    
    
############################################################################
 
import zmq  

context = zmq.Context()  
socket = context.socket(zmq.SUB)  
socket.connect("tcp://127.0.0.1:5000")  
socket.setsockopt(zmq.SUBSCRIBE,'')       #此操作之后的信息都可以订阅到

#获取一条订阅消息，如果订阅为空，则阻塞
socket.recv()     
