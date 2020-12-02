#coding:utf-8
import threading

import time


class MyThread(threading.Thread):
    def __init__(self,a):
        self.a=a
        super(MyThread, self).__init__()
    
    def run(self):
        """start时实际调用的函数"""
        time.sleep(1)
        print(self.a)


def f():
    t_list=[]
    for i in range(10):
        t=MyThread(i)
        t.start()
        t_list.append(t)
        
    for t in t_list:
        t.join()
    

if __name__=="__main__":
    f()

