#coding:utf-8
#python>=3.5 3.X全部支持？
"""
Annotations 函数注释
"""

def f(a:int)->int:
    print(type(a))
    return a


f(111)     #
f("aa")    #参数类型匹配也支持

#查看函数注释
f.__annotations__   
