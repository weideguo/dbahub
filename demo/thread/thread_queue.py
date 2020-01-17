#!/bin/env python
#coding:utf8
#multi thread control demo

import threading
import Queue
import time
import random

queue =  Queue.Queue()

def func(x):
    #如果不指定为全局变量 则需要在参数中单独引入 否则出现未指定引用
    #queue=x
    global queue
    while True:
        try:
            item = queue.get()
            sleep_time=random.randint(1,10)
            print("%s begin..... %s " % (item, sleep_time))
            time.sleep(sleep_time)
            print("%s end ...........%s" % (item, sleep_time))
        finally:
            #有多少个put即可执行多少task_done，可以在get之后或者直接执行
            queue.task_done()
    
    #这里不会被执行 why？        
    print("%s finish " % (item))


def main():
    #queue =  Queue.Queue()
    #并发数
    thread_num_concurrent=3
	
    #可以做到同时只启动对应数目的线程
    for i in range(thread_num_concurrent):
        t = threading.Thread(target=func, args=(queue,))
        #不设置则导致线程不会被结束 执行到最后线程时会一直阻塞
        t.setDaemon(True)
        t.start()

    #全部线程数
    thread_num=20
    for l in range(thread_num): 
        queue.put(l)
    
    print("all begin")
    #阻塞直到所有的queue执行完task_done()
    queue.join()
    print("all done")

if __name__=='__main__':
	main()
