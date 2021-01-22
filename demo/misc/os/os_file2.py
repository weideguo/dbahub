#文件锁     
import time
import fcntl

filename="zzz"
f=open(filename,"a+")

def x():
    #f=open(filename,"a+")                             #也可以单独在其他进程执行
    fcntl.lockf(f, fcntl.LOCK_EX)
    print("begin "+str(time.time()))
    time.sleep(3)
    print("done" +str(time.time()))
    fcntl.lockf(f, fcntl.LOCK_UN)


#from threading import Thread as Concurrent            #线程之间不生效
from multiprocessing import Process as Concurrent
t1=Concurrent(target=x)
t2=Concurrent(target=x)
t1.start()
t2.start()



"""
LOCK_UN - unlock
LOCK_SH - acquire a shared lock
LOCK_EX - acquire an exclusive lock
"""

#essentially a wrapper around the fcntl() locking calls
fcntl.lockf(f, fcntl.LOCK_EX)

fcntl.lockf(f, fcntl.LOCK_UN)        
        
#Perform the requested operation on file descriptor fd.        
fcntl.fcntl(f, fcntl.LOCK_EX)

fcntl.fcntl(f, fcntl.LOCK_UN)      

#Perform the lock operation op on file descriptor fd. flock(3)
fcntl.flock(f, fcntl.LOCK_EX)
fcntl.flock(f, fcntl.LOCK_UN)

       
#Perform the requested operation on file descriptor fd        
fcntl.ioctl(f, fcntl.LOCK_EX)

fcntl.ioctl(f, fcntl.LOCK_UN)            
        
                    