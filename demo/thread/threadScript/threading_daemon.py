# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 调用setDaemon()方法,测试守护线程，主线程退出时，守护线程是否还执行

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
