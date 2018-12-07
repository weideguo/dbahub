
'''
字符串在python内部表示是unicode
decode是将其他编码转换成unicode
encode是将unicode转换成其他编码


直接输入的string常量会用系统缺省的编码方式来编码

r raw
u 字符串是unicode编码的字符串


string object
unicode object
'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')   #文件的编码为utf8


a="中文"            #在GBK编码下输入 a的编码为               '\xd6\xd0\xce\xc4'
b=a.decode('gbk')   #由GBK转成unicode                      u'\u4e2d\u6587'

a="中文"            #在utf8编码下输入 a的编码为              '\xe4\xb8\xad\xe6\x96\x87'
b=a.decode('utf8')  #由utf8转成unicode                     u'\u4e2d\u6587'

a=u"中文"           #无论处于哪种编码环境 a的编码均为unicode  u'\u4e2d\u6587'
b=a.encode('utf8')  #由unicode编码转成utf8编码              '\xe4\xb8\xad\xe6\x96\x87'
b=a.encode('gbk')   #由unicode编码转成gbk编码               '\xd6\xd0\xce\xc4'

#只要包含coding 及 utf8 即可
#coding=utf8                     
# -*- coding: utf-8 -*- 
