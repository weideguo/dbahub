import time
import random
import threading


n=0
lock = threading.Lock()

"""
def updatex():
    global lock 
    lock.acquire()
    
    global n
    n=n+1
    time.sleep(random.random())
    print n
    
    lock.release()
    
"""
"""
def updatex():
    global lock
    with lock:
        global n
        n=n+1
        time.sleep(random.random())
        print n

"""

def updatex():
    global n
    n=n+1
    time.sleep(random.random())
    print n


t_list=[]
for i in range(10):
    t=threading.Thread(target=updatex,args=())
    t_list.append(t)

for t in t_list:
    t.start()

for t in t_list:
    t.join()
