#coding=UTF-8 
from http.server import HTTPServer,BaseHTTPRequestHandler  
import io,shutil  
  
class MyHttpHandler(BaseHTTPRequestHandler):  
	def do_GET(self):  
		response_str="Hello World"  
		enc="UTF-8"  
		response_encoded = response_str.encode(enc)  
		#f = io.BytesIO()  
		#f.write(encoded)  
		#f.seek(0)  
		self.send_response(200)
		#响应头部		
		self.send_header("Content-type", "text/html; charset=%s" % enc)  
		self.send_header("Content-Length", str(len(response_encoded))) 
		self.send_header("author", "weideguo")
		self.end_headers() 
		#响应体
		self.wfile.write(response_encoded)
		#shutil.copyfileobj(f,self.wfile)  
  
httpd=HTTPServer(('',8080),MyHttpHandler)  
print("Server started on 127.0.0.1,port 8080.....")  
httpd.serve_forever()  