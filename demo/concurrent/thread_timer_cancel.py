# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 定时器线程，调用Timer方法。

import logging
import threading
import time

logging.basicConfig(
    level = logging.DEBUG,
    format = '[%(levelname)s] (%(threadName)-10s) %(message)s',
    
)

def f():
    logging.debug('worker running')
    time.sleep(5)
    logging.debug('worker end')


def x(i):
    #Time类继承与Thread类
    #在一定时间后启动线程
    t1 = threading.Timer(3,f)  
    t1.setName('t1')
    t2 = threading.Timer(3,f)
    t2.setName('t2')
    
    
    t1.start()
    t2.start()
    logging.debug('waiting for thread start')
    
    time.sleep(i)
    logging.debug('canceling %s',t2.getName())
    t2.cancel()     #只有Time类创建的线程可以用于结束 未启动前才能cancel
    logging.debug('done')


if __name__ == "__main__":
    x(2)          #由于线程未启动 cancel生效
    #x(4)         #由于线程已经启动 cancel不再生效

