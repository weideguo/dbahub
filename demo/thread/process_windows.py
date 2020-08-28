#coding:utf8

"""
Add support for when a program which uses multiprocessing has been frozen to produce a Windows executable. 
windows系统使用多进程时
只能在脚本模式运行
"""
from multiprocessing import Process, freeze_support
x="xxxx"
def f(x):
    print(x)
    print('hello world!')

if __name__ == '__main__':
    freeze_support()
    Process(target=f,args=(x,)).start()



