"""
base64编码
6-bit截取字符串，映射成2^6=64个字符
如果字符串位数不是6的整数，则补到6与字符数的最小共倍数

如字符串只有一字节，为8位，则在后面补0到24位

base64编码串大小写敏感
"""  
  
a=u"中文".encode("utf8")  
  
  
b=base64.b64encode(a)     #转成base64编码 
 
base64.b64decode(b)       #base64编码转成可读格式




"""
base32
5-bit截取字符串，映射成2^5=32个字符
如果字符串位数不是5的整数，则补到5最小共倍数
base32编码串都为大写

"""

a="aakjdferhk"

b=base64.b32encode(a)  #转成base32编码

base64.b32decode(b)    #base32编码转成可读模式


"""
base16
4-bit截取字符串，映射成2^4=16个字符，即转成16进制
base16编码串都为大写
"""
a="aakjdferhk"

b=base64.b16encode(a)   
base64.b16decode(b)
