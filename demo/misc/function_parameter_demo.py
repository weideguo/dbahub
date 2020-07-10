
def func1(arg1,arg2=value2,...)     ##提供默认值              定义: f(x,y=2) 调用：f(12) / f(12,11)
def func1(*arg)                     ##传入多个参数            定义：f(*x)    调用：f(1,2,3,...)
def func1(**arg)                    ##                        定义：f(**x)   调用：f(x=1,y=2,z=3,...)





def f1(*a):
    print(a)

f1("p1","p2","p3")
#("p1","p2","p3")


def f2(**a):
    print(a)

f2(p1="v1",p2="v2")
#{"p1":"v1", "p2":"v2"}



"""
** 即将list tuple 类型转换 
y=("a","b","c")
*y 等同于
"a","b","c"
"""
def f3(a,b,c):
    print(a,b,c)

y=("a","b","c")
f3(*y)
#f1("a","b","c")      #等同于这样调用



"""
** 即将dict类型转换 
x={"a":"aaa","b":"bbb"}
**x 等同于
a="aaa", b="bbb"
"""
def f4(a,b):
    print(a,b)

x={"a":"aaa","b":"bbb"}
f4(**x)
#f(a="aaa", b="bbb")  #等同于这样调用


