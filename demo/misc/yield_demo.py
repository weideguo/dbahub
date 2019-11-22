#生成器 generator

def f(n):
    for i in range(n):
        yield i*i
			
			
a=f(10)
for x in a:
    print x


#############################
#协程 coroutine

import time

def f1():
    while True:
        a=yield 10
        time.sleep(10)
        print a


ff=f1()
a0=ff.next()      #获取f1()的下一个yield返回值
n1=ff.send(1)     #向f1()的下一个yield传送一个参数(yield关键字左边参数获取)；并获取yield的返回值（yield关键字右边）。执行过程会阻塞
                  #send 之后才会切换到下一个yield，即next和send对同一个yield生效
ff.close()        #关闭 
 

##############################


def A():
    yield
    print 1
    yield
    print 2
    yield
    print 3
    yield
    print 4


def B():
    yield
    print "a"
    yield
    print "b"
    yield
    print "c"
    yield
    print "d"


a1=A()
b1=B()
a1.next()
b1.next()

a1.next()
b1.next()

a1.next()
b1.next()

a1.next()
b1.next()
















