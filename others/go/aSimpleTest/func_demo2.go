package main

import "fmt"


func main() {

    // 匿名函数
    func(x int) {
        fmt.Println(x)
    }(100)


    // 匿名函数
    f := func(x int,y int) {
        fmt.Println(x, y)
    }

    f(100,200)
}
