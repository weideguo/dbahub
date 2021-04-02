import base64
base64.b64encode('__import__')

'X19pbXBvcnRfXw=='.decode('base64')


def make_secure():
    """
    移除模块
    """
    UNSAFE = ['open',
              'file',
              'execfile',
              'compile',
              'reload',
              '__import__',
              'eval',
              'input']
    for func in UNSAFE:
        try:
            del __builtins__.__dict__[func]
        except:
            pass



#通过特殊方式引入file模块
__builtins__.__dict__['file']=().__class__.__bases__[0].__subclasses__()[40]



"".__class__.__mro__[-1].__subclasses__()


#引入open
my_open="".__class__.__mro__[-1].__subclasses__()[40]
filename="/tmp/x.txt"
my_open(filename).read()


#可以通过查看不同模块继承的父类实现限制模块的引入



import sys

sys.modules['os']=None
import os       #失败 os模块已经不能引入

#sys.modules['os']






class A():
    __a = 1
    b = 2
    def __c(self):
        print("asd")
    def d(self):
        print('dsa')


x=A()

#查看对象的属性
dir(x)

#可以通过 下划线+类名+函数名 实现访问私有属性
x._A__a

#正常格式的私有属性不可访问
x.__a











