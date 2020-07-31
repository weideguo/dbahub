#coding:utf8

#随机字符
import random
chr(random.randint(65, 90))
"""
chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
"""
"""
使用系统的随机数生成方法 如 unix/linux的 /dev/urandom 
"""
random = random.SystemRandom()

#从 /dev/urandom  读取指定长度从而实现随机数生成
os.urandom(10)


