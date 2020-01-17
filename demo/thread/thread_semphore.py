# _*_ coding:utf-8 _*_

import logging
import threading
import random
import time

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s (%(threadName)-2s) %(message)s',
    
)


def f(s):
    with s:
        x=int(random.random()*10)
        logging.debug("begin,sleep %s" % x)    
        time.sleep(x)
        logging.debug("end")

def f2(s):
    s.acquire()
    x=int(random.random()*5)
    logging.debug("begin,sleep %s" % x)    
    time.sleep(x)
    logging.debug("end")
    s.release()



def t():
    # Semaphore初始化多少，即可以同时进行多少次acquire
    # 默认为1 即起到的效果跟Lock相同
    # 可用于并发控制 但线程依然全部启动
    s = threading.Semaphore(2)
    for i in range(4):
        t = threading.Thread(target=f2,args=(s,))
        t.start()

def t2():
    # Lock只能同时进行一次acquire
    s = threading.Lock()
    for i in range(4):
        t = threading.Thread(target=f2,args=(s,))
        t.start()


if __name__=="__main__":
    t()
    #t2()






