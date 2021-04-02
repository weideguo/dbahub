#coding:utf8
from __future__ import unicode_literals

#实现python2中对python3字符的兼容
#运行环境为python3则不进行改变


a="中文"        

b=b'\xe4\xb8\xad\xe6\x96\x87'   
a==b                            #默认python2字符串的存储格式为二进制   

c=u'\u4e2d\u6587'        
a==c                            #通过引用future模块，可以实现字符串为unicode


