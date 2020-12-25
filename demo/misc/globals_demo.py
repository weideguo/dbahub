#coding:utf8

#全局名字空间
print(globals())

a=111
b="ccc"

print(globals())

#全局名字空间设置参数
globals()["c"]="cccc"

print(c)

"""

全局名字空间 存储全局变量
局部名字空间 存储局部变量
闭包名字空间 存储闭包变量
内建名字空间 存储内置变量, 比如 int、str
"""
