###定义一个空类；也可直接定义函数
class Student0(object):     
	pass

###定义一个函数作为实例方法
def set_age(self, age):    
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student)   		### 给实例绑定方法
Student.set_age = MethodType(set_age, s, Student) 	### 给类绑定方法

class Student1(object):             
	__slots__ = ("name", "age")     ###限制类只有指定的属性，只对当前的类有效，对继承子类无限制


class Student2(object):
    """
    负责把一个方法变成属性调用。
    s.score 获取返回值
    """
    @property 					
    def score(self):
        return "bbb"
    
    """
    不需初始化类即可直接调用 Student.read()
    """
    @staticmethod
    def read(self):
        return "aaaa"
        
    """
    使用
    s=Student.my_init()
    s.score
    """
    @classmethod
    def my_init(cls,*args,**kwargs):
        #相当于调用构造函数
        return cls(*args,**kwargs)

