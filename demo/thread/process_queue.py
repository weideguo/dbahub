#coding:utf8
#from Queue import Queue
from multiprocessing import Queue

from multiprocessing import Process
import random
import time

from threading import Thread

my_queue=Queue(2)


def func(n,x):
    #my_queue=x
    global my_queue
    my_queue.put(1)
    x=int(random.random()*10)
    print("the process is %s sleep %s" % (n,x))
    time.sleep(x)
    print("process %s finish" % n)
    my_queue.get(1)
 
 
def p():
    #进程模型 
    #进程之间变量不共享。
    #但multiprocessing.Queue 可以在进程之间共享
    #Queue.Queue不能在进程之间共享 只能用于线程模型
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
    #线程间变量共享。
    #但multiprocessing.Queue Queue.Queue 都能用于线程模型
    t_list=[]
    for i in range(10):
        t = Thread(target = func, args = (i,my_queue))
        t_list.append(t)
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()
    print("all process finish")


if __name__ == "__main__":    
    #t()
    p()
    


