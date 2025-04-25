"""
Abstract Base Classes
定义接口规范，确保子类必须实现指定的方法。
解决鸭子类型可能导致的隐式接口问题，提供显式约束。
"""

from abc import ABC, abstractmethod

class Myabc(ABC):
    def __init__(self, s):
        self.s = s
    
    #@abstractmethod
    #def abstract_test(self, s):
    #    raise NotImplementedError
   
    def f1(self, s):
        print(s)


# 抽象类、存在抽象方法，
# 类不能初始化
#a = Myabc("A")

# 非抽象类、存在抽象方法
# 类可以初始化，但不能调用抽象方法
#a.abstract_test("a")

# 抽象类、不存在抽象方法
# 类可以初始化


class Mytest(Myabc):
    # 需要先覆盖抽象方法，新的类才能初始化
    def abstract_test(self, s):
        print(s)
    
    def f2(self, s):
        print(s)


t = Mytest("T")
t.abstract_test("t")
t.f1("t")
t.f2("t")
 
 

###############
class A():
    def f1(self):
        print("aaaaa1")
    def f2(self):
        print("aaaaa2")

class B():
    def f1(self):
        print("bbbbb1")
    def f2(self):
        print("bbbbb2")


def fx(o):
    o.f1()
    o.f2()


a = A() 
fx(a)

b = B() 
fx(b)

"""
鸭子类型
看起来像鸭子，吃起来像鸭子，就可以认为是鸭子
类A、类B都实现了相同的方法，因此可以当同一种类型使用
"""
