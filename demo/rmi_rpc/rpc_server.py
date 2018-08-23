from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

def add(x,y):
	return x+y
	
#class RequestHandler(SimpleXMLRPCRequestHandler):
#	rpc_path=('/RPC2',)
#s=SimpleXMLRPCServer(('127.0.0.1',8080),requestHandler=RequestHandler)
#s.register_function(add,'add')
if __name__=='__main__':
	s=SimpleXMLRPCServer(('127.0.0.1',8080))
	s.register_function(add)
	s.serve_forever()
