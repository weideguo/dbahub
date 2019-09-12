class Student(object):     ###定义一个空类；也可直接定义函数
	pass
	
def set_age(self, age):    ###定义一个函数作为实例方法
	self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s, Student)   		### 给实例绑定方法
Student.set_age = MethodType(set_age, s, Student) 	### 给类绑定方法

class Student(object):             
	__slots__ = ("name", "age")     ###限制类只有指定的属性，只对当前的类有效，对继承子类无限制

class Student(object):

    @property 					### @property装饰器就是负责把一个方法变成属性调用。即可使用s.score=70调用函数以及获取返回值
    def score(self):
        return self._score