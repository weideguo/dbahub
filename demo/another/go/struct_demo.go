package main

import "fmt"

// go 没有class关键字

func main() {
    // type 可以将各种基本类型定义为自定义类型
    // 在此定义Point 为一个结构体
    type Point struct {
        x int
        y int
    }
    var p Point
    p.x = 100
    p.y = 200
    fmt.Println(p.x)
    fmt.Println(p)

    p1 := new(Point)
    p1.x = 101
    p1.y = 201
    fmt.Println(p1.x)
    fmt.Println(p1)
}
