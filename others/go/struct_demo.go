package main

import "fmt"

// go 没有class关键字

// type 可以将各种基本类型定义为自定义类型
// 在此定义Point 为一个结构体
type Point struct {
    x int
    y int
}

func f1(){  
    //x :=Point{1,2}           //取实际实例
    x :=&Point{1,2}            //取实例的地址，访问时应该使用*取得对应值，但通过语法糖，可以省略
    fmt.Println(*x, (*x).x, (*x).y)
    fmt.Println(x, x.x, x.y)
    x.x=100
    x.y=200
    fmt.Println(x, x.x, x.y)
}


func f2(){ 
    var p Point
    // p := &Point{}
    // p := new(Point)

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

func main(){
    f1()
    //f2()
    
}
