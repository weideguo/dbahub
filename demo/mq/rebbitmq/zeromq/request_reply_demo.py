#请求响应模式



import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#会阻塞直至有请求被接收
message = socket.recv()

data="reply data"
#回应请求，没有阻塞；必须先有接收才能回应，否则会失败
socket.send(data)


############################################################


import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

data = "request data "
#如果远端没有接收，则发送失败
socket.send(data)

#如果远端没有发送，则接收失败    
response = socket.recv()
