# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 派生线程，调用其run()方法

import logging
import threading

logging.basicConfig(
	level = logging.DEBUG,
	format = '(%(threadName)-10s) %(message)s',
	
)

class MyThread(threading.Thread):

	def run(self):
		logging.debug('running')
		return

for i in range(5):
	t = MyThread()
	t.start()



