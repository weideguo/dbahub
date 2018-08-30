# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 调用join()方法

import logging
import threading
import time

logging.basicConfig(
	level = logging.DEBUG,
	format = '(%(threadName)-10s) %(message)s',
	
)


def daemon():
	logging.debug('Starging')
	time.sleep(2)
	logging.debug('Exiting')


d = threading.Thread(name='daemon',target=daemon)
d.setDaemon(True)

def non_daemon():
	logging.debug('Starting')
	logging.debug('Exiting')

t = threading.Thread(name='non-daemon',target=non_daemon)

d.start()
t.start()

d.join()
t.join()
