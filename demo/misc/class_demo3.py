#coding:utf8
#类默认值的设置


class X():
    a=[]                           #这种方式设置类默认值，创建对象时对此的修改影响到类的默认值，下一次创建对象查看到修改后的值
    def append(self,y):
        self.a.append(y)
        

x=X()
x.append(1)                        
x.a

x1=X()                             #
x1.a                               # 获取到之前创建对象对此的设置值



class Y():
    def __init__(self):
        self.a=[]
        
    def append(self,y):
        self.a.append(y)


y=Y()
y.append(1)
y.a

y1=Y()
y1.a                              #不会受到之前创建对象的影响



