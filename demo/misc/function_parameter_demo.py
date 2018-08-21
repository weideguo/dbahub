def f1(*a):
    print a
'''
(p1,p2,p3)
'''

def f2(**a):
    print a
'''
{p1:v1,p2:v2}
'''

f1(p1,p2)
f2(v1=p1,v2=p2)


'''
当a为{a:123,b:234}
**a为a=123,b=234
'''

def func1(arg1,arg2=value2,...)  ##提供默认值 		 定义: f(x,y=2) 调用：f(12) / f(12,11)
def func1(*arg)		         ##传入多个参数		定义：f(*x)    调用：f(1,2,3,...)
def func1(**arg)	         ##			     定义：f(**x)   调用：f(x=1,y=2,z=3,...)
