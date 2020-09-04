package main

import (
    "fmt"
    "json"
)

/*
控制反转  不用直接调用函数或对象，而是借助框架代码进行间接的调用和初始化
依赖注入  控制反转是一种设计思想，那么依赖注入就是这种思想的一种实现，通过注入参数或实例的方式实现控制反转
*/

func fl() {
    fmt.Println ("this is fl")
}
func f2 () {
    fmt.Println ("this is f2")
}

func normal_demo(){
    funcs := make(map[string] func ())
    funcs["fl"] = fl
    funcs["f2"] = f2
    //funcs["f3"] = "eeee"    //不同类型插入则失败
    funcs["fl"]()
    funcs["f2"]()
    fmt.Println(funcs) 
}





func main(){
    normal_demo()
    
}

