# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 使用with lock不需要显示地获得和释放锁。

import logging
import threading

logging.basicConfig(
	level = logging.DEBUG,
	format = '[%(levelname)s] (%(threadName)-10s) %(message)s',
	
)

def worker_with(lock):
	with lock:
		logging.debug('Lock acquired via with')

def worker_no_with(lock):
	lock.acquire()
	try:
		logging.debug('Lock acquired directly')
	finally:
		lock.release()


lock = threading.Lock()
w = threading.Thread(target=worker_with,args=(lock,))
nw = threading.Thread(target=worker_no_with,args=(lock,))

w.start()
nw.start()
