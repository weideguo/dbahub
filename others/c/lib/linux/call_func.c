#include<stdio.h>

int main()
{
    printf("call func()");
    func();
}

/*

动态链接 运行时需要外部库	
gcc func.c -shared -fPIC -o libfunc.so
gcc call_func.c -L. -lfunc  -o call_func        #调用so，libfunc.so放在与call_func.c同一目录


1.可以把当前路径加入 /etc/ld.so.conf中然后运行ldconfig，或者以当前路径为参数运行ldconfig（要有root权限才行）。
2.把当前路径加入环境变量 LD_LIBRARY_PATH 中

export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
确保动态链接库存在，然后再运行
*/


/*
静态链接 运行时不再依赖外部库
1. gcc -c func.c 
2. ar -r libfunc.a func.o   #把目标文件归档    
3. 
gcc call_func.c -L. -lfunc -static -o func.static  #在程序中链接静态库
gcc call_func.c -L. libfunc.a  -o func.static      #这个也可以

编译后可以直接运行 不再需要静态链接
*/



