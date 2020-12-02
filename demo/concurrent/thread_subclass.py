# /usr/bin/env python
# _*_ coding:utf-8 _*_

import logging
import threading

logging.basicConfig(
    level = logging.DEBUG,
    format = '(%(threadName)-10s) %(message)s',
    
)

class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')
        


class MyThreadWithArgs(threading.Thread):
        
    def __init__(self,group=None,target=None,name=None,args=(),kwargs=None,verbose=None):
        threading.Thread.__init__(self,group=group,target=target,name=name,verbose=verbose)
        self.args=args
        self.kwargs = kwargs
        
    #start实际调用的函数
    def run(self):
        logging.debug('running with %s and %s',self.args,self.kwargs)
        


def t1():
    for i in range(5):
        t = MyThread()
        t.start()

def t2():
    for i in range(5):
        t = MyThreadWithArgs(args=(i,),kwargs={'a':'A','b':'B'})
        t.start()


if __name__ == "__main__":
    #t1()
    t2()



