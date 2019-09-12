#coding=utf-8
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
	def handle(self):      
		self.data = self.request.recv(1024).strip()
		print("wrote:",format(self.client_address[0]))
		print(self.data)       
		self.request.sendall(self.data.upper())
#
#也可以选择这种，似乎不行
#class MyTCPHandler(socketserver.StreamRequestHandler):
#    def handle(self):
#        self.data = self.rfile.readline().strip()
#        print("wrote:",format(self.client_address[0]))
#        print(self.data)     
#        self.wfile.write(self.data.upper())

class MyUDPHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data = self.request[0].strip()
		socket = self.request[1]
		print("wrote:",format(self.client_address[0]))
		print(data)
		socket.sendto(data.upper(), self.client_address)
		
if __name__ == "__main__":
	HOST, PORT = "localhost", 9999
	#TCP服务端
	server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
	#UDP服务端
	#server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
	server.serve_forever()
	
