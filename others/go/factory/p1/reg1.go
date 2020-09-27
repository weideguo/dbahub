package p1
import (
    "../base"
    "fmt"
)

type Class1 struct {
}

func (c *Class1) Do() {
    fmt.Println("this is function of Class1")
}
func init() {
    // 将名称 与 实例化方法 注册到工厂 
    base.Register("Class1", func() base.Class {
        return new(Class1)
    })
}
