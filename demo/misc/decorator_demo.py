#装饰器
#coding=utf-8

def decorator1(func):
    def my_wrapper():		
        print "bDFGER"
        func()
    return my_wrapper

	
#不可接受任何参数	
@decorator1
def f1():
    print 'rr'
	
######################################################   

def decorator2():
    def _decorator2(func):
        def my_wrapper():           
            print "bDFGER"
            func()
        return my_wrapper
    return _decorator2

    
#不可接受任何参数
@decorator2()
def f2():
    print 'yyy'   
    
     
######################################################     
   
def decorator3(func): 
    def my_wrapper(*a,**b):
        print a
        print b
        func(*a,**b)
    return my_wrapper

    
#函数可以接受参数 装饰器不可以接受参数
@decorator3
def f3(*a,**b):
    print a
    print b

f3('ref','re',rf='rtb',g='r')




######################################################  
from functools import wraps

def decorator31(func):
    @wraps(func)
    def my_wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return my_wrapper    


@decorator31
def f31(*a,**b):
    """
    help(f31) 可以查看原函数的定义
    """
    print(a)
    print(b)
  
help(f31)
f31('ref','re',rf='rtb',g='r')

################################################################################    
    
def decorator4(x=None):
    print x,1                 #使用@decorator4时即调用
    def _decorator4(func):
        print x,2             #使用@decorator4时即调用
        return func
    return _decorator4  
   

#装饰器 函数的参数都可以有 装饰器内获取只能获取装饰器函数的参数
@decorator5('yyy')
def x(n,m):
    print n,m
   

##############################################################################

def decorator5(x=None):
    print x,1                   #使用@decorator5时即调用
    def _decorator5(func):
        print x,2               #使用@decorator5时即调用
        def my_wrapper(*a,**b):
            print x,3           #调用被装饰的函数时才调用
            print a
            print b	
            func(*a,**b)
        return my_wrapper
    return _decorator5


#装饰器 函数的参数都可以有 而且可以在装饰器内获取
@decorator5(x='wert')		
def x(t):
	print t
    
