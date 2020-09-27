package main

import "fmt"

func main() {
    // 声明与赋值
    var a int
    a=10
    
    // 声明与赋值
    var b int =100

    // 变量可以直接声明并赋值，编译时自动推断
    c := 1000
    d := "10000" 
    
    fmt.Printf("%d \n" , a)
    fmt.Printf("%d \n" , b)
    fmt.Printf("%d \n" , c)
    fmt.Printf("%s \n" , d)
}
