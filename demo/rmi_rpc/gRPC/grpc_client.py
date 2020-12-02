#!/usr/bin/env python
# -*- coding: utf-8 -*-
#gRPC client

#from __future__ import print_function

import grpc
from helloworld_pb2 import HelloRequest, HelloReply
from helloworld_pb2_grpc import HelloWorldServiceStub


def run(server_address):
    
    with grpc.insecure_channel(server_address) as channel:
        # rpc通信
        stub = HelloWorldServiceStub(channel)
        # 调用服务端定义的方法
        response = stub.SayHello(HelloRequest(name="wwwww"))
    
    print("client received: " + response.message)

if __name__ == "__main__":
    server_address="127.0.0.1:50000"
    run(server_address)