#coding:utf8
from threading import Thread
import time
from Queue import Queue
import random

def func(n,my_queue):
    my_queue.put(1)
    x=int(random.random()*10)
    print("the thread is %s"%n)
    time.sleep(x)
    print("thread %s finish"%n)
    my_queue.get(1)


def func1(n,y):
    global my_queue
    my_queue.put(1)
    x=int(random.random()*10)
    print("the thread is %s"%n)
    time.sleep(x)
    print("thread %s finish"%n)
    my_queue.get(1)


if __name__ == "__main__":
    my_queue=Queue(2)
    thread_list=[]
    for i in range(10):
        t = Thread(target = func1, args = (i,my_queue))
        thread_list.append(t)
    
    #线程全都被启动 即通过 ps -T $pid 可以查看到所有线程
    #通过线程内部的阻塞实现并发控制
    for th in thread_list:
        th.start()
        
    for th in thread_list:
        th.join()
    print("all thread finish")
