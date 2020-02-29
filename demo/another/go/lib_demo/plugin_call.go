package main

import (
    "fmt"
    "plugin"
)

func main() {

    //加载动态库
    p, err := plugin.Open("plugin.so")
    if err != nil {
        panic(err)
    }
    
    //查找函数   
    f, err := p.Lookup("DCall")
    if err != nil {
        panic(err)
    }
    //转换类型后调用函数 不转换则不能调用   
    f.(func())()
    
    f2, err := p.Lookup("DCallWithParam")
    if err != nil {
        panic(err)
    }
    //带参函数的调用
    f2.(func(string))("hello world,plugin.so")

    
    f3, err := p.Lookup("DCallWithReturn")
    if err != nil {
        panic(err)
    }
    r :=f3.(func(string)string)("function with return call")
    fmt.Println("return from plugin function call: ", r)
}    
