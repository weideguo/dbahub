package main

import (
    "fmt"
    "plugin"
)

func main() {

    p, err := plugin.Open("plugin_demo.so")
    if err != nil {
        panic(err)
    }
    m, err := p.Lookup("Func1")
    if err != nil {
        panic(err)
    }
    res := m.(func(int) int)(30)
    fmt.Println(res)
}
/*
#编译成so文件
go build -buildmode=plugin plugin_demo.go
#使用so文件提供的函数
go build main.go
*/