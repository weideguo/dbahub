#coding:utf8

from dis import dis
dis("print(1)")
#打印出执行的字节码
#disassemble

def add(a,b):
    return a+b

dis(add)
