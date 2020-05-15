from struct import *


name, serialnum, school, gradelevel="myname",1234,5,6
r=pack('<6sHHb',name, serialnum, school, gradelevel)
unpack('<6sHHb', r)



"""
struct.pack(format, v1, v2, ...)          #转换成二进制串 以string格式输出
struct.unpack(format, buffer)             #转换成字符串   以tuple格式输出





###格式
#Standard siz
'<', '>', '!','='

Character   "Byte order" 
@            native 
=            native 
<            little-endian        小端  二进制格式从低位开始计算（即左边开始）
>            big-endian           大端  二进制格式从高位开始计算（即右边开始）
!            network (= big-endian) 




#native size
Format "C Type"
x      pad byte 
c      char  
b      signed char  
B      unsigned char  
?      _Bool  
h      short  
H      unsigned short  
i      int  
I      unsigned int  
l      long  
L      unsigned long  
q      long long  
Q      unsigned long long  
n      ssize_t  
N      size_t  
e      (6) 
f      float  
d      double  
s      char[]  
p      char[]  
P      void *



#使用native size可以不用@为开头

###################################################
> 大端
< 小端
大端模式是指数据的低位保存在内存的高地址中，而数据的高位保存在内存的低地址中.
小端模式是指数据的低位保存在内存的低地址中，而数据的高位保存在内存的高地址中。


"""



