
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


#只要包含coding 及 utf8 即可
#coding=utf8                     
# -*- coding: utf-8 -*- 
