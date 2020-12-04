#coding:utf8
#
#base64编码 映射成 字母大小写+数字+"+"+"/"
#如果字符串位数不为6（2^6=64）的倍数，尾部补0
#编码后字符串为4的倍数，不够则补"="

import base64

src=u"中文也可以"
src=src.encode('utf-8')                   #unicode->utf8 byte  需要给函数传入byte类型

base64_str=base64.b64encode(src)
print(base64_str)

base64.b64decode(base64_str)


