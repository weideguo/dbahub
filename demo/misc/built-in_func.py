#coding:utf8
#一些built-in方法的说明

#########################################################
dir()    #列出当前模块的变量、方法和定义的类型列表


"""
def f():
    pass

f.xx="xxxx"    #函数也可以当成对象执行设置属性   
   
class A():
    pass
"""
dir(f)  #列出指定对象的的变量、方法和定义的类型列表

dir(A)


#########################################################
"""
cat > model_name.py << EOF
class MyClass():
    pass

EOF
"""
#通过模块的字段串名字指定引入
import model_name
MyClass=getattr(model_name,"MyClass")

#类似于
#from model_name import MyClass


