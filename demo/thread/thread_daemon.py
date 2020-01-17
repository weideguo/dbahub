# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 调用setDaemon()方法,测试守护线程，主线程退出时，守护线程是否还执行

import logging
import threading
import time
import random

#logging模块线程安全 即可以控制同时只有一个线程占用
logging.basicConfig(
    level = logging.DEBUG,
    format = '(%(threadName)-10s) %(message)s',
    
)


def f():
    logging.debug('Starging')
    i=random.randint(1,5)
    time.sleep(i)
    logging.debug('Exiting')




def x():
    d = threading.Thread(name='daemon',target=f)
    d.start()
    
    print("parent done")     #不会被阻塞
    #执行父进程任务结束后等待线程任务


def x1():
    d = threading.Thread(name='daemon',target=f)
    d.setDaemon(True)        #父进程结束时同时结束线程
    d.start()
    
    print("parent done")     #不会被阻塞
    #执行父进程任务结束后直接结束后台线程
    

def x2():
    d = threading.Thread(name='daemon',target=f)
    d.setDaemon(True)         #父进程结束时同时结束线程
    d.start()
    d.join()                  #阻塞至线程结束
    
    print("parent done")


def x3():
    d = threading.Thread(name='daemon',target=f)
    d.setDaemon(True)         #父进程结束时同时结束线程
    d.start()
    d.join(1)                 #可以设置阻塞超时时间
    
    print("parent done")


def x4():
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()
    
    #获取活动Thread实例的列表
    for t in threading.enumerate():
        
        #主线程不能join 要跳过
        if t is threading.currentThread():    
            continue              
        
        logging.debug('joining %s',t.getName())
        t.join()                  #阻塞至该线程结束
    
    #可以实现等待后台线程
    print("parent done")


if __name__ == "__main__":
    #x()
    #x1()
    #x2()
    #x3()
    x4()



