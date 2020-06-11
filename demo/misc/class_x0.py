"""
python2 类默认继承于 type    #旧类 旧式类实行的是深度优先，先从继承数的左侧开始深入最底寻找，然后再找右侧
python3 类默认继承于 object  #新类 广度优先，先进行水平的寻找
先继承的优先
"""

class A():
    def f(self):
        print("aaaa")

class B():
    def f(self):
        print("bbb")

class C(A,B):
    pass

c=C()
c.f()  #先继承于A，则以A的方法优先

##############################################

class AA():
    def f(self):
        print("aaaa1111")

class BB():
    pass


class A(AA):
    pass

class B(BB):
    def f(self):
        print("bbb")


class C(A,B):
    pass


c=C()
c.f()   #都是以深度优先

##############################################

#class AA(object):
class AA():
    def f(self):
        print("aaaa1111")


class A(AA):
    pass

class B(AA):
    def f(self):
        print("bbb")


class C(A,B):
    pass


c=C()
c.f()     
#python2 以深度优先 即方法继承于 AA
#python3 以广度优先 即方法继承于 B
#如果 AA继承于 object，则都以广度优先