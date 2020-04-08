#调用linux的动态链接库
from ctypes import *

# 加载动态连接库
test = cdll.LoadLibrary('./libtest.so')

test.test()
add =test.add
add.argtypes =[c_float, c_float]      #设置输入参数类型
add.restype =c_float                  #设置返回类型
print(add(1.3, 13.4))


#调用libc库
libc = cdll.LoadLibrary('/usr/lib64/libc.so.6')
#查看动态库拥有的函数
#nm libc.so.6 |grep printf  
#查看函数定义
# /usr/include

#调用libc的函数
libc.printf("aaa")    

libc.time(0)

libc.random()

abs=libc.abs
abs.retype=c_int
abs.argtypes=[c_int]
abs(-100)

"""
类型转换
c     python  ctypes
char  string  c_char  
int   int     c_int
float float   c_float

https://docs.python.org/3/library/ctypes.html
"""

"""
cat > ./test.c << EOF
#include "test.h"

void test(){
  printf("hello so\n");
}

float add(float a, float b){
  return a+b;
}
EOF


cat > ./test.h << EOF
#include "stdio.h"

void test();
float add(float, float);
EOF


#编译成动态链接库
gcc -fPIC -shared test.c -o libtest.so

#静态链接库要编译成动态链接库再使用
#gcc -fPIC -c test.c       #编译(必须加-fPIC才能打包成动态库)
#ar -cru libtest.a test.o  #打包成静态库
ar -x libtest.a                   #解压静态库获得可执行文件
gcc -shared test.o -o libtest.so  #将可执行文件打包成动态库
"""



