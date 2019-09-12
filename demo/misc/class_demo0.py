
'''
zabbix_api
├── workdir
│   ├── get_zabbbix_value.py
│	├── __init__.py
│   └── yyy.py					# import  get_zabbbix_value
└──  xxx.py        				# impoer workdir.get_zabbbix_value
'''


#继承
class Mammal(Object):
	pass

class Dog(Mammal):				 #单继承
    pass
	
class Dog(Mammal, Runnable):     #多重继承
    pass


#定制类

class Student(object):
	def __init__(self, name):		 #类可以传参数进行初始化	
		self.name = name
	def __str__(self):				 #可以使用print(Student("name"))
		return 'Student object (name: %s)' % self.name	
	__repr__ = __str__               
	
#直接显示变量调用的不是__str__()，而是__repr__()	
#__str__()   ###返回用户看到的字符串，
#__repr__()  ###返回程序开发者看到的字符串
#__name__()  ###获取函数名
#_main_

#语句用来在脚本中判断是否在【执行python模块】或者【导入python模块】
#if __name__='__main__'			
#如果导入模块(python文件)，则__name__不为__main__;如果执行，则为__main__。



class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 	# 初始化

    def __iter__(self):
        return self 			# 迭代自己；  用于 for n in Fib():

    def __getitem__(self, n):   #用于类可以像数组一样使用；如Fib()[0]
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
		
	def next(self):
        self.a, self.b = self.b, self.a + self.b 	# 计算下一个值
        if self.a > 100000: 						# 退出循环的条件
            raise StopIteration();
        return self.a 								# 返回下一个值