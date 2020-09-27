package main

import "fmt"


// &T{} 取结构体T的地址

type Co struct {
    name string
    comment *string

    // 以下写法等价
    // comment *string
    // comment*string
    // comment* string
    // comment * string
}

func f() {
 
    t := &Co{}
    
    t.name="www"
    y := "this is comment"
    t.comment = &y
    
    // 通过语法糖实现 (*t).name 与 t.name 等价
    fmt.Println((*t).name)
    fmt.Println(t.name)
    

    fmt.Println(t.comment)
    // 以下形式等价
    fmt.Println(*t.comment)
    fmt.Println(* t.comment)
    fmt.Println(*(t.comment))
    fmt.Println(* (t.comment))
    
    // 结构体初始化
    t1 := &Co{name:"yyyy",comment:&y}
    fmt.Println(t1)
    
    t2 := &Co{"yyyy",&y}
    fmt.Println(t2)
}

//结构体没有构造函数的功能，使用结构体初始化的过程来模拟实现构造函数
func newCo(name string,comment *string) *Co{
    return &Co{name,comment}
    
}

func f2(){
    y := "this is comment"
    c :=newCo("yyyy",&y)
    fmt.Println(c)
}


func main() {

    //f()
    f2()
}
