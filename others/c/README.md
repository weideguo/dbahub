# 编译时
## 头文件头使用顺序
  
1、编译时参数 -I
 
2、gcc的环境变量 C_INCLUDE_PATH,CPLUS_INCLUDE_PATH,OBJC_INCLUDE_PATH （windows下对应include环境变量）
 
3、内定目录
/usr/include
/usr/local/include
/usr/lib/gcc

  
装gcc的时候，是有给定的prefix，则
/usr/include 
$prefix/include


使用格式 
#include <xxx>   // 这种方式用于标准或系统提供的头文件，到保存系统标准头文件的位置查找头文件。
#include "xxx"   // 这种方式常用于引用自己的头文件。先查找当前目录是否有指定名称的头文件，然后在从标准头文件目录中查找。

 

## 库文件使用顺序

1、编译时参数 -L -l 

2、gcc的环境变量LD_LIBRARY_PATH

3、/etc/ld.so.conf中指定的动态库搜索路径  运行 ldconfig 使更该生效
 
4、内定目录 /lib /usr/lib /usr/local/lib  这是当初编译gcc时写在程序内的



# 运行时 

## 运行时动态库的搜索的先后顺序是：

1、在编译目标代码时指定该程序的动态库搜索路径（还可以在编译目标代码时指定程序的动态库搜索路径。
这是通过gcc 的参数"-Wl,-rpath,"指定。当指定多个动态库搜索路径时，路径之间用冒号":"分隔

2、通过环境变量LD_LIBRARY_PATH指定动态库搜索路径（当通过该环境变量指定多个动态库搜索路径时，路径之间用冒号":"分隔）（HP-UX对应的是SHLIB_PATH环境变量，AIX对应的是LIBPATH环境变量，windows对应的是lib环境变量）
  
3、在配置文件/etc/ld.so.conf中指定动态库搜索路径

4、默认的动态库搜索路径/lib /usr/lib

##  链接库
动态链接 运行时需要外部库
静态链接 运行时不再依赖外部库  



# demo
```
linux C++
newcpp.h     ###头文件，包含类的声明，函数的声明
newcpp.cpp	 ###主函数文件，通过头文件使用类、函数
func.cpp     ###类函数的实现，包含头文件

#编译成动态链接库
g++ func.cpp -fPIC -shared -o libcall_func.so                 
#使用动态链接库
g++ newcpp.cpp -o newcpp  -L/root/src/lib -lcall_func_so    

#指定使用的头文件编译
g++ -shared -fPIC -I /usr/include/mysql -o call_func_add.so call_func_add.cpp
```