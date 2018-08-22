#!/usr/local/python/bin/python
# -*- coding: utf-8 -*-

import time
import traceback
from multiprocessing import Process,Pool,Queue
from threading import Thread
	
def t_func(thred_queue,a):
    thred_queue.put(1)
    print "thread  begin"
    time.sleep(100)
    print a
    print "thread end"
    thred_queue.get()

my_queue=Queue()

def p_advance():
    print "this is advance process"
    thred_queue=Queue(2)
    while True:
        a=my_queue.get()
        if a != 100:
            my_thread=Thread(target=t_func,args=(thred_queue,a))
            my_thread.start()
            
        else:
            break
    my_thread.join()
    print "advance process end"
		
			

def p_func(i,my):
    print "process begin"
    
    my_queue.put(i)
    time.sleep(100)
    
    print "process end"


if __name__ == '__main__':
    
    my_pool=Pool(3)
    #my_queue=Queue()
    my=''
    for i in  range(5):
        my_pool.apply_async(func=p_func,args=(i,my))
    my_process=Process(target=p_advance,args=())
    my_process.start()	
    my_pool.close()
    my_pool.join()
    my_queue.put(100)
    #my_process.start()		
    my_process.join()
    
    print "all complete"
