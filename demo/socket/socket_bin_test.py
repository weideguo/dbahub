#!/usr/bin/python
#coding:utf8
import socket
import struct
import os
import time

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 51001)) 
    server.listen(1)
    while (1):
        conn,client = server.accept()
        conn.settimeout(5000)         #
        msg = conn.recv(4)            #total data length
        if len(msg) <= 0:             #
            continue
        data = struct.unpack("i", msg)
        print "Recv Total length:%d"%(data[0])
        process_len = 0 
        msg = conn.recv(data[0])
        for i in range(0,4):          #url title content author
            para = msg[process_len:(process_len + 4)] 
            if len(para) < 4:         
                continue
            data = struct.unpack("i", para)
            str_len = data[0]
            print "%d"%(str_len)
            para = msg[(process_len + 4):(process_len + 4 + str_len)]
            if len(para) < str_len:   
                continue
            data = struct.unpack("%ds"%(str_len), para)
            print "%s"%(data[0])
            process_len = process_len + 4 + str_len 
        conn.close()
