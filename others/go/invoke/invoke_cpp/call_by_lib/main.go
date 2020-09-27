package main
/*
#cgo CFLAGS: -Icpp
#cgo LDFLAGS: -L. -lfunc
#include "cwrap.h"
*/
import "C"
func main() {
    C.call()
}

/*
编译动态链接库
gcc cwrap.cpp test.cpp -shared -fPIC -o libfunc.so

将动态链接库以及头文件放入指定的位置

使用#cgo定义库路径
-L.     链接库的位置
-lfunc  链接库的名字 libXXX.so

编译
go build

运行
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:`pwd`
./xxx

编译后依赖动态链接库才能运行
*/


/*
编译静态态链接库
gcc -c test.cpp cwrap.cpp 
ar -cru libfunc.a cwrap.o test.o 

go build生成的可执行文件不再需要连接库才能运行
*/
