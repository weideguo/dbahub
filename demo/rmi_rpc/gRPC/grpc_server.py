#!/usr/bin/env python
# -*-coding: utf-8 -*-
#gRPC server
#
#预先编译proto文件
#python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. helloworld.proto
#

from concurrent import futures
import time
import grpc


from helloworld_pb2_grpc import add_HelloWorldServiceServicer_to_server,HelloWorldServiceServicer
from helloworld_pb2 import HelloRequest, HelloReply


# 定义
class Hello(HelloWorldServiceServicer):

    def SayHello(self, request, context):
        return HelloReply(message="Hello, %s!" % request.name)


def serve(bind_address):
    # 通过thread pool来并发处理server的任务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    add_HelloWorldServiceServicer_to_server(Hello(), server)
    
    server.add_insecure_port(bind_address)
    #add_secure_port TLS/SSL安全连接
    
    server.start()
    
    #用于接收控制台的ctrl+c
    try:
        while True:
            time.sleep(60 * 60 * 24)
            
    except KeyboardInterrupt:
        server.stop(0)
        #stop(self, grace)


if __name__ == "__main__":
    bind_address="[::]:50000"
    print("listen at: %s " % bind_address)
    print("ctrl+c to terminal")
    serve(bind_address)


