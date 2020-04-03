#coding:utf8
import os

#如果使用os.chdir() 则获取改变之后的目录
#获取当前文件的目录，当被其他模块调用时也可使用
p=os.path.dirname(os.path.abspath(__file__))
print(p)

#获取进程当前工作目录
p1=os.getcwd()
print(p1)

#切换进程工作目录
os.chdir("/tmp")
p2=os.getcwd()
print(p2)
