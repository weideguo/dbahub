package demo

/*
一个目录下的同级文件归属一个包。
包名可以与其目录不同名。
包名为 main 的包为应用程序的入口包，编译源码没有 main 包时，将无法编译输出可执行的文件。

首字母都为小写，这些标识符可以在包内自由使用，但是包外无法访问它们
包外访问需要首字母为大写
*/


import (
    "fmt"
)
func PrintStr() {
    fmt.Println("go go go")
}
