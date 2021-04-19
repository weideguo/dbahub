package main

import "fmt"

type Co struct {
    name string
    comment *string
}


func update(b *Co, x string,y *string) {
    b.name = x
    b.comment = y
}


// 接收器
// func (接收器变量 接收器类型) 方法名(参数列表) (返回参数)
// 为结构体添加方法
func(c *Co) update(x string,y *string) {
    c.name = x
    c.comment = y
    //是以下的语法糖
    //(*c).name = x
    //(*c).comment = y
}

func f4(){
    c := new(Co)
    y := "yyyyy111"
    //以下两种方法实现效果一样
    //update(c,"mmm111", &y)
    c.update( "mmm111", &y)
    fmt.Println(c)
}

type MyInt int

// 为任意数据类型添加方法
func(m MyInt) isZeo() bool {
    return m ==0
}

func f5(){
    var x MyInt
    x=0
    fmt.Println(x.isZeo())
}

func main() {

    f4()
    f5()    
}
