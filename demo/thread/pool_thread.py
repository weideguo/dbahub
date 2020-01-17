#!/usr/local/python/bin/python
# -*- coding: utf-8 -*-
#coding: utf8
import time
import traceback
from multiprocessing import Pool
from threading import Thread

    
def t_func(ip,it):
    print("process %s thread %s begin"%(ip,it))
    time.sleep(100)
    print("process %s thread %s end"%(ip,it))


def p_func(ip):
    print("process begin")
    threads=[]
    for it in range(10):
        my_thread=Thread(target=t_func,args=(ip,it))
        threads.append(my_thread)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print("process end")


if __name__ == '__main__':
    
    my_pool=Pool(3)
        
    for i in  range(5):
        my_pool.apply_async(func=p_func,args=(i,))
    my_pool.close()
    my_pool.join()

    print("all complete")
