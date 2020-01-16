#coding:utf8
import time
import random
from threading import Thread,Lock
from multiprocessing import Process

n=0
lock = Lock()


def update():
    #不进行任何加锁操作 
    #不指定为全局变量 则导致变量未声明出错
    global n
    
    x=random.random()
    time.sleep(x)
    n=n+1
    print(n)         #所有线程获取的变量值都一样
    

def update1():
    global n
    
    x=random.random()
    time.sleep(x)
    global lock
    with lock:
        n=n+1
        print(n)         


def updatex():
    global lock 
    lock.acquire()   
    
    #传入0可以实现非阻塞获取
    #is_lock = lock.acquire(0)
    
    global n
    n=n+1
    time.sleep(random.random())
    print(n)
    
    lock.release()
    

def updatex1():
    global lock
    with lock:
        global n
        n=n+1
        time.sleep(random.random())
        print(n)


def t():
    #线程之间变量共享
    #在线程之间全局变量都互相影响
    t_list=[]
    for i in range(10):
        t=Thread(target=update,args=())
        t_list.append(t)
    
    for t in t_list:
        t.start()
    
    for t in t_list:
        t.join()
        
        
def p():
    #进程之前变量不共享 
    #在此全局变量在每个进程之间都是独立的
    p_list=[]
    for i in range(10):
        p=Process(target=update1,args=())
        p_list.append(p)
    
    for p in p_list:
        p.start()
    
    for p in p_list:
        p.join()        
            
            
if __name__ == "__main__":
    t()
    #p()
            
            
            
            
            
            
            
            
            
            
            
            

