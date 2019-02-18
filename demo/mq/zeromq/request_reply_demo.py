#zeromq不需要依赖第三方服务，无需启动其他程序
#请求响应模式


import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#会阻塞直至有请求被接收          可以接收多个客户端的消息 但必须回应请求后才能再次接收
message = socket.recv()

data="reply data"
#回应请求，没有阻塞；必须先有接收才能回应，否则会失败
socket.send(data)


############################################################


import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

data = "request data "
#不阻塞 如果远端没有接收，则发送失败
socket.send(data)

#阻塞 如果没有本地请求发送，则接收失败    
response = socket.recv()
