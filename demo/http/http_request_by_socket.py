#coding=utf-8
import socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	#建立连接
	s.connect(("www.hao123.com",80))
	#请求行
	request_line="GET /index.html HTTP/1.1"
	#请求首部,多个使用"\r\n"分隔
	headers="Host:www.hao123.com\r\nContent-Type:text/html"
	#空行，标记请求首部结束
	blank_line="\r\n"
	#请求体
	request_body="a=b&c=d"
	#组合成请求信息
	message="\r\n".join([request_line,headers,blank_line,request_body])
	#b'GET /index.html HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n'
	s.send(message.encode('utf-8'))
	response=s.recv(10240)
	print(response)

	


#'''
#HTTP请求
#	请求行
#		请求方法
#			GET POST PUT
#		请求URL
#			/index.html
#		HTTP协议版本
#			HTTP/1.1
#	请求首部
#	空行
#		\r\n
#	请求体
#
#【请求行/请求首部/空行/请求体】之间使用"\r\n"分隔
#
#
#HTTP响应
#	响应行(HTTP/1.1 200 OK)
#		HTTP协议版本
#		状态码
#		状态码描述
#	响应首部
#	空行
#	响应体
#'''

















