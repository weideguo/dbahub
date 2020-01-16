#coding:utf8
#协程 coroutine
#线程是操作系统层面的“并行”， 协程是应用程序层面的“并行”。


import time

def f1():
    while True:
        a=yield 10
        #time.sleep(10)    #会导致执行过程阻塞
        import asyncio     # python >= 3.4
        asyncio.sleep(10)  #执行过程不阻塞
        print(a)

if __name__ == "__main__":
    ff=f1()
    a0=ff.next()        #获取yield返回值 不会导致下一步执行  预激
    n1=ff.send(1)       #向yield传送一个参数(yield关键字左边参数获取)；并获取下一个yield的返回值（yield关键字右边）。
                        #send 之后才会切换到下一个yield，即next和send对同一个yield生效
    ff.close()          #关闭 
 