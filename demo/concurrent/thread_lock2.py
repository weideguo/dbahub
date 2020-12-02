# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 使用Lock对象控制对共享资源的访问

import logging
import threading
import time
import random

logging.basicConfig(
    level = logging.DEBUG,
    format = '[%(levelname)s] (%(threadName)-10s) %(message)s',
    
)

class Counter(object):
    def __init__(self,start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        
        logging.debug('Acquired lock')
        self.value = self.value + 1
        
        self.lock.release()


def worker(c):
    pause = int(random.random()*10)
    logging.debug('Sleeping %s' % pause)
    time.sleep(pause)
    c.increment()
    logging.debug('Done')



if __name__ == "__main__":
    counter = Counter()
    for i in range(4):
        t = threading.Thread(target=worker,args=(counter,))
        t.start()
    
    logging.debug('Waiting for worker threads')
    for t in threading.enumerate():
        if t is not threading.currentThread():
            t.join()
     
    logging.debug('Counter: %d',counter.value)
    logging.debug('all done')













