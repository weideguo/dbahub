#Parallel Pipeline
#
#一个pull对应对各push
import zmq

context = zmq.Context()

socket = context.socket(zmq.PULL)
socket.bind('tcp://*:5558')

#阻塞获取一条消息，可以接收多个客户端的发送
socket.recv()



###############################################################################

   

import zmq

context = zmq.Context()

recive = context.socket(zmq.PULL)
recive.connect('tcp://127.0.0.1:5557')

sender = context.socket(zmq.PUSH)
sender.connect('tcp://127.0.0.1:5558')

#阻塞获取一条消息
data = recive.recv()

#不阻塞发送消息
sender.send(data)


################################################################################
    
    
#一个push对应多个pull
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind('tcp://*:5557')

data = "push data"
#不阻塞，发送消息给一个客户端 如果存在多个客户端则轮询
socket.send(data)
