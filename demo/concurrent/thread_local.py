# /usr/bin/env python
# _*_ coding:utf-8 _*_

import logging
import threading
import random

logging.basicConfig(
	level = logging.DEBUG,
	format = '(%(threadName)-10s) %(message)s',
	
)

def show_value(data):
	try:
		val = data.value
	except AttributeError:
		logging.debug('No value yet')
	else:
		logging.debug('value=%s',val)

def worker(data):
	show_value(data)
	data.value = random.randint(1,100)
	show_value(data)

class MyLocal(threading.local):
	def __init__(self,value):
		logging.debug('Initializing %r',self)
		self.value = value



def t1():
    local_data = MyLocal(1000)   #所有线程获取到的资源都为在此设置，线程之前的修改不互相影响
    show_value(local_data)

    for i in range(4):
        t = threading.Thread(target=worker,args=(local_data,))
        t.start()


def t2():
    #默认线程间数据互相影响
    #local可实现线程之前的数据不会相互影响
    local_data = threading.local()
    local_data.value = 1000     #只对主线程有效 其他线程依然获取到原始值 即为没有设置
    show_value(local_data)
    
    for i in range(2):
        t = threading.Thread(target=worker,args=(local_data,))
        t.start()

def t3():
    #默认线程间数据互相影响
    #local可实现线程之前的数据不会相互影响
    #local_data = threading.local()
    class Data():
        value=1000
    
    local_data=Data()
    
    show_value(local_data)
    
    for i in range(2):
        t = threading.Thread(target=worker,args=(local_data,))
        t.start()

if __name__ == "__main__":
    t1()
    #t2()
    #t3()






