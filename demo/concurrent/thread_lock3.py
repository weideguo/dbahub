# /usr/bin/env python
# _*_ coding:utf-8 _*_


import threading


#同步锁 Lock
l.threading.Lock()
l.acquire(blocking=True, timeout=1)
l.release()


#递归锁
#类似于同步锁 Lock
#在同步锁的基础上可以做到连续重复使用多次acquire()后再重复使用多次release()的操作（同步锁则不行）
#但加锁次数和解锁次数必须一致，否则也将引发死锁现象
l=threading.RLock()




#条件锁
l=threading.Condition()
l.wait(timeout=None)                  #等待notify
l.wait_for(predicate, timeout=None)   #predicate为一个可调用对象，且返回结果为bool类型，为true则继续运行
l.notify(n=1)                         #通知wait，n则为多个
l.notify_all()                        #通知所有wait





#事件锁
#一次只能放行全部
l=threading.Event()
l.clear()                   #将事件锁设为红灯状态，即所有线程暂停运行
l.set()                     #将事件锁设为绿灯状态，即所有线程恢复运行   可以多次调用set clear
l.is_set()                  #用来判断当前事件锁状态，红灯为False，绿灯为True
l.wait(timeout=None)        #将当前线程设置为“等待”状态，只有该线程接到“绿灯通知”或者超时时间到




#信号量锁
l=threading.Semaphore(value=1)           #value为多少则同时可以acquire多少，用于并发控制
l.acquire(blocking=True, timeout=1)
l.release()



#条件锁：一次可以放行任意个处于“等待”状态的线程
#事件锁：一次可以放行全部的处于“等待”状态的线程
#信号量锁：通过规定，成批的放行特定个处于“上锁”状态的线程


#list、tuple、dict本身就是属于线程安全

