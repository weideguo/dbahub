#coding=UTF-8 
import os   #Python的标准库中的os模块包含普遍的操作系统功能  
import re   #引入正则表达式对象  
import urllib   #用于对URL进行编解码  
from http.server import HTTPServer, BaseHTTPRequestHandler  #导入HTTP处理相关的模块  
#from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler  
  
#自定义处理程序，用于处理HTTP请求  
class TestHTTPHandler(BaseHTTPRequestHandler):  
#处理GET请求  
	def do_GET(self):   
		response_str ='''   
<html>   
<head>   
<title>QR Link Generator</title>   
</head>   
<body>    
<br>   
<br>   
<form action="/qr" name=f method="GET"><input maxLength=1024 size=70   
name=s value="" title="Text to QR Encode"><input type=submit   
value="Show QR" name=qr>   
</form> 
</body>   
</html> 
'''  
		#设置协议版本 
		self.protocal_version = 'HTTP/1.1'
		#设置响应状态码 
		self.send_response(200)
		#设置响应头
		self.send_header("Welcome", "Contect") 
		self.end_headers() 
		#输出响应内容  
		self.wfile.write(response_str.encode('utf-8'))
  
def start_server(port): 
	#HTTPServer的构造函数__init__(server_address, RequestHandlerClass, bind_and_activate=True)
    http_server = HTTPServer(('', int(port)), TestHTTPHandler)  
    http_server.serve_forever()  
  
#os.chdir('static')  #改变工作目录到 static 目录  
start_server(8000) 