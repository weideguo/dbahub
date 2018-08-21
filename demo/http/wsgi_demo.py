#!/bin/env python
#coding:utf8

from wsgiref.simple_server import make_server

def app(environ,start_response):
    start_response("200 OK",[("Content-Type","text/html"),("Server","wdg web server")])
    #start_response(self, status, headers, exc_info=None)
    print environ          #请求的参数
    return "hello!"

if __name__ == "__main__":
    httpd=make_server('',8000,app)
    print "start server on port 8000"
    httpd.serve_forever()
