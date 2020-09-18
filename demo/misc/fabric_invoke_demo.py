#coding:utf8
#fabric 使用 invoke 库
#命令行工具 提供命令行调用


# 文件名：tasks.py
from invoke import task

@task
def hello(c):
    print("Hello world!")

@task
def greet(c, name):
    c.run("echo %s" % name)



#在本地执行shell
#inv greet xxx
#inv hello


