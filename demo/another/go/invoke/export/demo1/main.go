
package main
 
/*
#include <stdio.h>
int add(int a, int b);
*/
import "C"
 
import (
    "fmt"
)
 
//当使用export的时候，在同一个文件中就不能再定义其它的c函数了，不然会报错。
//使用export导出函数给c语言调用。
 
//export GoAdd
func GoAdd(a, b int) int {
    return a + b
}
 
func main() {
    a := C.add(1, 2)
    fmt.Printf("C.add(1,2) return %d\n", a)
}
