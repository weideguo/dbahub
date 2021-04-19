package main

import "fmt"

//自定义类型
type Xtype int

//自定义类型可以设置函数 类似于结构体
func(x Xtype) Square() int {
    y := x * x
    return int(y)
}

func main(){
    var x Xtype = 100
    fmt.Println(x)
    fmt.Println(x.Square())
}
