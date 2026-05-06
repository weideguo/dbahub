#-*-encoding:utf-8-*-
#回调函数


def f1():
	return 20

def f2():
	return 30

def fx(func):
	print(func())


fx(f1)   #输出20
fx(f2)	 #输出30



