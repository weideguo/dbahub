#coding:utf8
from collections import defaultdict

d=defaultdict(set) #设置d为字典且字典的值为set
#d={}              #使用该方式则不能做到如下

d['a'].add("aaa") #字典的值默认为set
d['a'].add("bbb")
d['b']="BBB"      #也可以直接覆盖原来的值

"""
>>> type(d['a'])
<class 'set'>
"""
