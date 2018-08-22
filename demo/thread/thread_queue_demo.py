#!/bin/env python
#coding:utf8
#multi thread control demo

import threading
import Queue
import time
import random


def func(queue):
    while True:
        try:
            item = queue.get()
            print item
            sleep_time=random.randint(1,10)
            print "%s begin....."%str(sleep_time)
            time.sleep(sleep_time)
            print "%s end ..........."%str(sleep_time)
        finally:
            #how many put() happen in queue，then how many task_done() can be used
            queue.task_done()


def main_func():
    queue =  Queue.Queue()	
    thread_num_concurrent=3
	
    for i in range(thread_num_concurrent):
        t = threading.Thread(target=func, args=(queue,))
        t.setDaemon(True)
        t.start()

    thread_num=20
    for l in range(thread_num): 
        queue.put(l)

    #block until all item in queue have been gotten
    queue.join()

if __name__=='__main__':
	main_func()
