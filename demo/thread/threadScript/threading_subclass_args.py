# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 派生线程，调用其run()方法,重新定义构造函数

import logging
import threading

logging.basicConfig(
	level = logging.DEBUG,
	format = '(%(threadName)-10s) %(message)s',
	
)

class MyThreadWithArgs(threading.Thread):
        
	def __init__(self,group=None,target=None,name=None,args=(),kwargs=None,verbose=None):
		threading.Thread.__init__(self,group=group,target=target,name=name,verbose=verbose)
		self.args=args
		self.kwargs = kwargs
		return


	def run(self):
		logging.debug('running with %s and %s',self.args,self.kwargs)
		return

for i in range(5):
	t = MyThreadWithArgs(args=(i,),kwargs={'a':'A','b':'B'})
	t.start()



