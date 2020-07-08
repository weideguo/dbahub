#定制类

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


class A(object):
    def __init__(self,*args,**kwargs):	 
        """
        控制这个初始化的过程。它是实例级别的方法，即先有__new__创建实例，然后运行对应__init__操作
        """
        print("__init__")
        self.name="aaa"
        
    
    def __new__(cls,*args,**kwargs):
        """
        控制生成一个新实例的过程。它是类级别的方法。先于__init__执行
        新类才有(即继承于object)
        """
        print("__new__")
        return super(A, cls).__new__(cls,*args,**kwargs)
 
 
#new方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。
class PositiveInteger(int):
    #而是用__init__则起不到不同样效果
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))

x=PositiveInteger(-10) 
 
# 单例模式  
class Singleton(object):  
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls,*args,**kwargs)
        return cls.instance


#多次实例化都只获取到一个实例
s1=Singleton()
s2=Singleton()
s1==s2


class A(object): 
    def __str__(self):
        """
        #print实例时的值
        c=A()
        print(c)
        """
        return "xxxx"
    
    
    def __repr__(self): 
        """
        #直接调用实例时的值
        c=A()
        c
        """
        return "xxx"
    
    
    def __del__(self,*args,**kwd): 				
        """
        c=A()
        del c       
        #释放对象，在对象被删除之前调用
        """ 
        print("object del")
    
    
    def __iter__(self):
        yield 1
        yield 2
        """
        #迭代自己获得的值
        for i in A():
            print(i)
        """
        
        
    def __getitem__(self, n):    
        """
        调用 A()[3] 
        """
        return n*n 
    
    def __missing__(self, key):
        """
        A()['aaa']  
        调用 __getitem__ 失败时 调用 __missing__
        """
        self[key]="xxx"
        return "xxx"
    
    
    def __len__(self)：
        """
        在调用内联函数len()时被调用
        c=A()
        len(c)
        """
        return 100

    
    def __call__(self,*args)	 		
        """
        把实例对象作为函数调用
        c=A()
        c()
        """
        print("call by object")
        
    
    def __enter__(self):
        """
        with 创建类时调用
        """
        print("with begin")
       
       
    def __exit__(self, exc_type, exc_val, exc_tb)     
        """
        with 结束类时调用
        """
        print("with end")
        


class A(object):
    
    def __init__(self,name):
        self.name=name
    
    def __cmp__(self, s):			
        """
        比较两个对象
        用于sorted() 
        """
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0


a_list=[A("ccc"),A("aaa"),A("bbb")]
#排序
sorted(a_list)
#比较
A("ccc")>A("aaa")



class A(object):
    
    def __init__(self,name):
        self.name=name
    
    def __eq__(self,other):			
        """判断self对象是否等于other对象"""
        return self.name == other.name
        
    """
    __gt__(self,other)				判断self对象是否大于other对象
    __lt__(slef,other)				判断self对象是否小于other对象
    __ge__(slef,other)				判断self对象是否大于或者等于other对象
    __le__(slef,other)				判断self对象是否小于或者等于other对象
    """
    
    
A("aaa")==A("bbb")
A("aaa")==A("aaa")


class A(object):  
    def __init__(self,a):
        self.a=a
        
    def __setattr__(self,name,value):	 	
        """设置实例属性时调用"""
        print(name,value)
        object.__setattr__(self, name, value)
    
    #__getattribute__(self,name): 	
    def __getattr__(self,name): 
        """
        #获取不存在的属性时调用
        a=A()
        print(a.b)
        """
        print("can not find attr: %s" % str(name))
    
    def __delattr__(self,name):
        """
        删除属性时实际调用
        a=A()
        del a.a
        """
        print("del attr: "+name)
        object.__delattr__(self,name)    



class A(object):
    pass

a=A()
#为对象 增加/查询/删除 属性
setattr(a,"a","aaa")
getattr(a,"a")
delattr(a,"a")
      
      
