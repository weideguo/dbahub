package main

import "fmt"

/*
#include<stdio.h>

void printString(const char* s, int n) {
    int i;
    for(i = 0; i < n; i++) {
        putchar(s[i]);
    }
    putchar('\n');
}
*/
import "C"
import "unsafe"
import "reflect"

func printString(s string) {
    p := (*reflect.StringHeader)(unsafe.Pointer(&s))
    C.printString((*C.char)(unsafe.Pointer(p.Data)), C.int(len(s)))
}
func main() {
    s := "hello"
    fmt.Println(s)
    printString(s)
}

// 需要 C/C++ 构建工具链
