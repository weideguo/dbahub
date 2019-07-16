#coding:utf8
#最简单webserver样例
from wsgiref.simple_server import make_server


def application(environ, start_response):
    # 响应的状态码与头部
    start_response('200 OK', [('Content-Type', 'text/plain;charset=UTF-8')])
    # environ 发起请求的所有数据
    #print str(environ)
    return str(environ)
       

  
server=make_server('0.0.0.0',8091,application)
server.serve_forever()
