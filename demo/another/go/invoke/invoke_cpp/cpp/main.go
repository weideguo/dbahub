package main
/*
#include "cwrap.h"
*/
import "C"
func main() {
    C.call()
}
/*
直接使用cpp的源码编译，但cpp的源码必须封装成c的格式
编译后不再依赖其他文件
*/
