
package main
 
/*
#cgo CFLAGS: -I .
#cgo LDFLAGS: -L . -lclibrary
#include "clibrary.h"
int callOnMeGo_cgo(int in);  //通过中间文件实现
*/
import "C"
 
import (
    "fmt"
    "unsafe"
)
 
//export callOnMeGo
func callOnMeGo(in int) int {
    return in + 1
}
 
func main() {
    fmt.Println("Go.main(): calling C function")
 
    //使用unsafe.Pointer转换
    C.some_c_func( (C.callback_fcn)( unsafe.Pointer(C.callOnMeGo_cgo) ) )
}

/*
gcc clibrary.c -shared -fPIC -o libclibrary.so
go build
*/
