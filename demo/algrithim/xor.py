#coding:utf8
#exclusive OR 异或

1^1
#0

0^0
#0


1^0
#1

0^1
#1

#转换成二进制后对比

100^10
"""
即为
bin(100) ^ bin(10)

'0b1100100'
   '0b1010'
   1101110
   
int('1101110',2)

"""


"""
应用
A为n-1个1到n的队列，求缺失的数
A[0] ^ A[1] ^ ... ^ A[n-2] ^ 1 ^ 2 ^ ... ^ n


加密
text ^ key = cipherText
解密
cipherText ^ key = text


数据备份 x文件与y文件产生z
x ^ y = z
还原 只要存在x/y其中一个，即可还原出另外一个
z ^ x = y
"""



