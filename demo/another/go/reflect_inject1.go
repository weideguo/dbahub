package main
import (
    "fmt"
    "reflect"
    "github.com/codegangsta/inject"
)
type S1 interface{}
type S2 interface{}
func Format(name string, company S1, level S2, age int) {
    fmt.Printf("name=%s, company=%s, level=%s, age=%d \n", name, company, level, age)
}
func main() {
    inj := inject.New()
    //实参注入 顺序必须确定
    inj.Map("tom")
    inj.MapTo("ttt", (*S1)(nil))
    inj.MapTo("T4", (*S2)(nil))
    inj.Map(333)
    //函数反转调用
    fmt.Println(inj)
    inj.Invoke(Format)
}
