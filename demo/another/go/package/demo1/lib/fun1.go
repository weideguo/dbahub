package mylib

import "fmt"

func F2(){
    F()       //同包下的文件的属性可以直接引用 等同于在一个文件内
    fmt.Println("function on other file2222")
}
