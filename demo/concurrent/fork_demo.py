# -*- coding: utf-8 -*-
import os										
import time
import random

print('Process (%s) start' % os.getpid())
pid = os.fork()									###只能在类unix系统使用

def f1():
    ###执行子进程操作
    print("Begin: child process (%s) parent is %s." % (os.getpid(), os.getppid()))     
    x=int(random.random()*10)
    time.sleep(10)
    #如果父进程先结束 则托管 即父进程的pid变为1
    print("End: child process (%s) parent is %s." % (os.getpid(), os.getppid()))  
    
    
def f2():
    ###执行父进程操作
    print("Begin: (%s) created child process (%s)."% (os.getpid(), pid))					
    x=int(random.random()*10)
    time.sleep(x)
    print("End: (%s) done"% os.getpid())


if pid==0:																					###由pid判断是子进程、父进程					
    f1()
else:
	f2()
'''
###fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
'''
