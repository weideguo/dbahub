#生成器 generator

def f(n):
    for i in range(n):
        yield i*i
			
			
a=f(10)
for x in a:
    print(x)


#############################
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


ff=f1()
a0=ff.next()      #获取yield返回值 不会导致下一步执行  预激
n1=ff.send(1)     #向yield传送一个参数(yield关键字左边参数获取)；并获取下一个yield的返回值（yield关键字右边）。
                  #send 之后才会切换到下一个yield，即next和send对同一个yield生效
ff.close()        #关闭 
 

##############################


def A():
    yield 11
    print(1)
    yield 22
    print(2)
    yield 33
    print(3)
    yield 44
    print(4)


def B():
    yield "aa"
    print("a")
    yield "bb"
    print("b")
    yield "cc"
    print("c")
    yield "dd"
    print("d")


a1=A()
b1=B()


############python 2
a1.next()
b1.next()

a1.next()
b1.next()

a1.next()
b1.next()

a1.next()
b1.next()

###########python3
next(a1)        #获取yield的返回值，但yield之后的操有不会继续执行
next(b1)
     
next(a1)        #函数由上一次yield继续执行到下一次yield，并返回
next(b1)
     
next(a1)
next(b1)
     
next(a1)
next(b1)



from inspect import getgeneratorstate

getgeneratorstate(a1)   #获取函数的状态









