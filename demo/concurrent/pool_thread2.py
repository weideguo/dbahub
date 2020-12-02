#!/usr/local/python/bin/python
# -*- coding: utf-8 -*-

import time
import traceback
from multiprocessing import Process,Pool,Queue
from threading import Thread
import random	
    
#multiprocessing下的Queue可以实现在多进程之间共享
#使用进程池生产 
#使用线程消费


p_queue=Queue()    


def thread_func(t_queue,a):
    t_queue.put(1)
    print("thread get %s begin" % a)
    time.sleep(random.randint(1,10))
    print("thread get %s end" % a)
    t_queue.get()


def process_func():
    print("customer process begin")
    t_queue=Queue(2)
    while True:
        a=p_queue.get()
        if a != 100:
            my_thread=Thread(target=thread_func,args=(t_queue,a))
            my_thread.start()
        else:
            break
    my_thread.join()
    print("customer process end")
		
 
def pool_func(i,):
    print("pool process begin put %s" % i)
    
    p_queue.put(i)
    time.sleep(random.randint(1,5))
    
    print("pool process end put %s" % i)


if __name__ == '__main__':
    
    my_pool=Pool(3)
    for i in  range(5):
        my_pool.apply_async(func=pool_func,args=(i,))
    
    my_process=Process(target=process_func,args=())
    
    my_process.start()	
    
    my_pool.close()
    my_pool.join()          #阻塞至所有pool的进程结束
    
    p_queue.put(100)
    my_process.join()
    
    print("all complete")
