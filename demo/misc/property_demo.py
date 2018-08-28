#/bin/env python

class Pdemo(object):
	def __init__(self,a,b):
		self.a=a
		self.b=b	
	
	@property
	def f1(self):
		return str(self.a)+str(self.b)

if __name__ == '__main__':
	p=Pdemo(5,6)
	print p.f1
