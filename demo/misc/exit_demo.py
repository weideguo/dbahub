#!/bin/env python
#coding:utf8
import sys
import time
from threading import Thread
from multiprocessing import Process


def f1():
    print("function1 begin")
    time.sleep(2)
    #exit(0)           #进程或线程使用时只结束当前的进程或线程
    sys.exit(0)        #进程或线程使用时只结束当前的进程或线程
    print("function1 end")

    
def f2():
    print("function2 begin")
    time.sleep(4)
    print("function2 end")
 
 
c1=Process(target=f1)      
c2=Process(target=f2)      
    
#c1=Thread(target=f1)    
#c2=Thread(target=f2)    

c1.start()
c2.start()

c1.join()
c2.join()
