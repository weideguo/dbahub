#coding:utf8
#函数中的特殊属性，func_code，函数中有很多以func_ 开头的属性



def f():
    print(1)


import dis

#汇编格式字节码
dis.dis(f)

#以下只适用python2
f.func_code.co_code
f.func_code.co_consts



