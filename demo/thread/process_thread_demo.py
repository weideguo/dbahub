#!/bin/env python
#coding:utf8

from multiprocessing import Process
import time
from threading import Thread,Lock
import threading
import random

a=0
def s_func_t(lock):
	lock.acquire()
	global a
	print a
	a=a+1
	time.sleep(3)
	print a
	lock.release()

def s_func():
	
	global a
	print a
	a=a+1
	
	time.sleep(3)
	print a
	

def test_p():
	a=0
	p_l=[]
	for i in range(10):
		p=Process(target=s_func,args=())
		p_l.append(p)
		
	for p in p_l:
		p.start()
	for p in p_l:
		p.join()
	
def test_t():
	lock=Lock()
	t_l=[]
	for i in range(10):
		t=Thread(target=s_func_t,args=(lock,))
		t_l.append(t)
	
	for t in t_l:
		t.start()
	for t in t_l:
		t.join()
	
if __name__=="__main__":
	#test_p()      	#进程不共享变量a
	test_t()		#线程共享变量a,如果需要顺序获取与修改，需要加锁
	
	
	
	

