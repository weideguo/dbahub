# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 调用set()和clear()、wait()实现线程间传送信号

import logging
import threading
import time

logging.basicConfig(
    level = logging.DEBUG,
    format = '[%(levelname)s] (%(threadName)-10s) %(message)s',
    
)

def wait_for_event(e):
    
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set one:%s',event_is_set)
    time.sleep(5)
    event_is_set = e.wait()
    logging.debug('event set two:%s',event_is_set)


def wait_for_event_timeout(e,t):
    
    while not e.isSet():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)   #设置超时等待时间
        logging.debug('event set: %s',event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


def tt():
    e = threading.Event()
    t1 = threading.Thread(name='block',target=wait_for_event,args=(e,))
    t1.start()
    
    time.sleep(3)
    e.set()         #设置为True wait操作获取值
    logging.debug('Event is set')
    e.clear()       #重新设置为False 依旧可以再次调用 e.set()
    


def tt2():
    e = threading.Event()
    t2 = threading.Thread(name='nonblock',target=wait_for_event_timeout,args=(e,2))
    t2.start()    

    time.sleep(5)
    e.set()
    logging.debug('Event is set')
  

if __name__ == "__main__":
    #tt()
    tt2()


