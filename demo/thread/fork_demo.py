import os										

# -*- coding: utf-8 -*-
print 'Process (%s) start' % os.getpid()
pid = os.fork()									###只能在类unix系统使用
if pid==0:																					###由pid判断是子进程、父进程					
    print("I am child process (%s) and my parent is %s." % (os.getpid(), os.getppid()))      ###执行子进程操作
else:
    print("I (%s) just created a child process (%s)."% (os.getpid(), pid))					###执行父进程操作
	
'''
###fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
'''
