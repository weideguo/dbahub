package main
import (
    "fmt"
    "github.com/codegangsta/inject"
)
type S1 interface{}
type S2 interface{}
type Staff struct {
    Name    string  `inject` 
    Company S1      `inject` 
    Level   S2      `inject`
    Age     int     `inject`
}
//用于注入的结构体的声明的属性必须包含tag `inject`，且属性类型必须全部不同

func main() {
    s := Staff{}
    
    inj := inject.New()
    
    //注入的顺序可以任意 通过类型自动匹配
    inj.Map(33)
    inj.Map("nnn")
    inj.MapTo("T4", (*S2)(nil))
    inj.MapTo("xxx", (*S1)(nil))  //这种注入的值可以为任意类型
    
    inj.Apply(&s)
    fmt.Printf("s= %v\n", s)
}
