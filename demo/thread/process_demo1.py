#coding:utf8
import os
import random
import time
from multiprocessing import Process
from threading import Thread

def f1():
    print(os.getpid())
    while True:
        print("f111111111")
        time.sleep(int(random.random()*10) )

def f2():
    print(os.getpid())
    while True:
        print("f22222222")
        time.sleep(int(random.random()*10) )

def f3():
    t=Thread(target=f1)
    t.start()
    t.join()

if __name__ == "__main__":

    #p1=Process(target=f1)
    p1=Process(target=f3)
    
    p2=Process(target=f2)
    
    p1.start()
    p2.start()
    
    print(p1.pid)
    print(p2.pid)
