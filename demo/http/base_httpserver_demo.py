#!/usr/env python
# -*- coding: UTF-8 -*-

import os   													
import re   													
import urllib   												
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler  	

class TestHTTPHandler(BaseHTTPRequestHandler):
    #GET  
    def do_GET(self):        
        print 'URL=',self.path
        
        templateStr = '''
        <html>   
        <head>   
        <title>QR Link Generator</title>   
        </head>   
        <body>   
        hello Python!
        </body>   
        </html>
        '''
    
        self.protocal_version = 'HTTP/1.1'  	
        self.send_response(200) 				 
        self.send_header("Welcome", "Contect")  
        self.end_headers()
        self.wfile.write(templateStr)   
    #POST	
    def do_POST(self):
        self.wfile.write("<p>this is post</p>")   #must in html format
		
		
def start_server(port):
    http_server = HTTPServer(('', int(port)), TestHTTPHandler)
    http_server.serve_forever() 

if __name__ == "__main__":
  start_server(8000)  			
