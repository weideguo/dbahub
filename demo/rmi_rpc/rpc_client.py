from xmlrpclib import ServerProxy

if __name__=='__main__':
	s=ServerProxy('http://127.0.0.1:8080')
	print s.add(3,4)
