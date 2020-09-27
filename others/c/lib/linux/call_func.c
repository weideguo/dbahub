#include<stdio.h>

int main()
{
    printf("call func()");
    func();
}

/*
#调用so，libfunc.so放在与call_func.c同一目录
gcc call_func.c -L. -lfunc  -o call_func
*/


/*
/usr/include            ##CentOS头文件目录

gcc/c++         
-I                      ##指定头文件位置
-L                      ##指定动态链接库的目录

*/


/*
动态连接库 运行时需要外部库
1.可以把当前路径加入 /etc/ld.so.conf中然后运行ldconfig，或者以当前路径为参数运行ldconfig（要有root权限才行）。
2.把当前路径加入环境变量 LD_LIBRARY_PATH 中
*/

/*
静态链接 运行时不再依赖外部库
1. gcc -c func.c 
2. ar -r libfunc.a func.o   #把目标文件归档    
3. 
gcc call_func.c -L. -lfunc -static -o func.static  #在程序中链接静态库
gcc call_func.c -L. libfunc.a  -o func.static      #这个也可以
*/


/*
linux C++
newcpp.h     ###头文件，包含类的声明，函数的声明
newcpp.cpp	 ###主函数文件，通过头文件使用类、函数
func.cpp     ###类函数的实现，包含头文件

#编译成动态链接库
g++ func.cpp -fPIC -shared -o libcall_func.so                 
#使用动态链接库
g++ newcpp.cpp -o newcpp  –L/root/src/lib –lcall_func_so    

#指定使用的头文件编译
g++ -shared -fPIC -I /usr/include/mysql -o call_func_add.so call_func_add.cpp
*/
