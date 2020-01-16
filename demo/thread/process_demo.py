#coding:utf8
from multiprocessing import Process
from threading import Thread
from Queue import Queue
import time
import random


my_queue=Queue(2)


def func(n,my_queue):
    my_queue.put(1)
    x=int(random.random()*10)
    print("the process is %s sleep %s" % (n,x))
    time.sleep(x)
    print("process %s finish" % n)
    my_queue.get(1)


def func1(n,y):
    global my_queue
    my_queue.put(1)
    x=int(random.random()*10)
    print("the process is %s sleep %s" % (n,x))
    time.sleep(x)
    print("process %s finish" % n)
    my_queue.get(1)


def p():
    #进程模型 
    #进程之间变量不共享。在此每个进程的my_queue会单独存在，彼此互不影响，因而在此实现不了进程控制
    process_list=[]
    for i in range(10):
        p = Process(target = func, args = (i,my_queue))
        process_list.append(p)
    for p in process_list:
        p.start()
    for p in process_list:
        p.join()
    print("all process finish")
 

def t(): 
    #线程模型 
    #线程之间全局变量互相影响。在此变量my_queue为同一个，因而在此可以实现线程控制
    t_list=[]
    for i in range(10):
        t = Thread(target = func1, args = (i,my_queue))
        t_list.append(t)
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()
    print("all thread finish")
 
    
if __name__ == "__main__":    
    #t()
    p()
    
    
    
    
    
