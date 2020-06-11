
a=100
#__class__  获取实例的类型
a.__class__
a.__class__.__class__

"""
class任然是一个object：
可以将其赋给一个变量
可以对其进行拷贝
可以赋给其新的变量
可以将其作为参数赋给其他的函数
"""
#object 不可继承, class 可以继承

def dynamic_class_creater(name):
    if name == 'name1':
        class class1(object):
            pass
        return class1
    else:
        class class2(object):
            pass
        return class2


#动态生产类可以继承
MyClass=dynamic_class_creater("xxx")
class B(MyClass):
    pass


"""
type的两种用法只是兼容 没有联系
type查看对象类型
type(my_object)

type可以动态创建class
type(class_name, tuple_of_parent_class, dict_of_attribute_names_and_values)


type(object) -> the object's type
type(name, bases, dict) -> a new type   #class即为type？
"""
def bbb(self):
    print("bbbb")

MyClass=type("MyClass",(object,),{"a":0,"b":bbb})

class A(MyClass):
    pass



"""
metaclass 类 对象
class = metaclass()
object = class()

type是Python定义好的metaclass，可以自定义metaclass。
"""


class Foo(object):
    """
    默认class使用type作为__metaclass__，即表明类的创建方法
    当前类的 __metaclass__ 不会被继承，子类继承当前类的母类的 __metaclass__
    __metaclass__ 可以为 type 或其子类，也可以为方法
    """
    __metaclass__ = type



########################################################################
def upper_attr(class_name, class_parents, class_attr):
    uppercase_attr = {}
    for name, val in class_attr.items():
        if name.startswith('__'):
            uppercase_attr[name] = val
        else:
            uppercase_attr[name.upper()] = val
    
    return type(class_name, class_parents, uppercase_attr)


class Foo(object):
    __metaclass__ = upper_attr
    bar = 'bar'


hasattr(Foo,"BAR")
hasattr(Foo(),"BAR")
########################################################################

#需要重载__new__而不是__init__
class UpperAttrMetaclass(type):
    def __new__(cls, cls_name, bases, attr_dict):
        uppercase_attr = {}
        for name, val in attr_dict.items():
            if name.startswith('__'):
                uppercase_attr[name] = val
            else:
                uppercase_attr[name.upper()] = val
        return super(UpperAttrMetaclass, cls).__new__(cls, cls_name, bases, uppercase_attr)


class Foo(object):
    __metaclass__ = UpperAttrMetaclass
    bar = 'bar'

hasattr(Foo,"BAR")
hasattr(Foo(),"BAR")
