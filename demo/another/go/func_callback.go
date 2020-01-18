package main

import "fmt"

// type  定义数据类型
// 在此定义Callback为一个函数
type Callback  func(x int, y int) int


// 回调函数
func f(x int,y int,callback Callback) int {
    s := callback(x,y)
    return s
}



func add(x int,y int) int{
    return x+y
}


func main() {
    r := f(1,2,add)
    fmt.Println(r)
}
