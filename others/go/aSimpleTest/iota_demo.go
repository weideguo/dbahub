package main

import "fmt"


const (
	a0 = iota                      // 数字自增常量 从0开始
	b0           
	c0          
)

const (
	a1 = 5* ( iota +1 )            // 可以使用自增值应用于表达式
	b1           
	c1          
)


const (
	a2 = 100                       // 100  const 后的变量可以只给第一赋值
	b2                             // 100
	c2                             // 100
)

const (
	a3 = iota                      // 0
	b3 = 100                       //
	c3 = iota                      // 2 中间存在其他非自增但后续又继续自增时
)

func main(){
    fmt.Printf("%d %d %d\n" , a0,b0,c0)
    fmt.Printf("%d %d %d\n" , a1,b1,c1)
    fmt.Printf("%d %d %d\n" , a2,b2,c2)
    fmt.Printf("%d %d %d\n" , a3,b3,c3)
}