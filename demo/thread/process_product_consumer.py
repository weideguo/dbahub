#!/bin.env python
#coding:utf8
#实现异步的生产消费模式
from multiprocessing import Queue,Process
import os,time,random

def write(q):
    for value in ['A','B','C']:
        print('write put: %s...'%value)
        q.put(value)
        sleep_time=random.random()*3
        time.sleep(sleep_time)
        #print('write put: %s...'%value)
        #q.put(value)

def read(q):
    while True:
        value = q.get(True)
        if value=="QUIT":
            print("read now quit.....")
            break
        else:
            print('read get: %s...'%value)
            

if __name__ == '__main__':
    print('start...')
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()

    pw.join()       #阻塞至pw结束
    q.put('QUIT')
    pr.join()       #阻塞至pr结束
    print('done...')
