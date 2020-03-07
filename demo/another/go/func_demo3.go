package main
import (
    "fmt"
)
func Accumulate(value int) func() int {
    //闭包（Closure）在某些编程语言中也被称为 Lambda 表达式
    //闭包的变量会跟随闭包生命期一直存在
    return func() int {
        value++
        return value
    }
}
func main() {
    accumulator := Accumulate(1)
    fmt.Println(accumulator())
    fmt.Println(accumulator())
    fmt.Println(accumulator())
    fmt.Printf("%p\n", &accumulator)
    
    accumulator2 := Accumulate(10)
    fmt.Println(accumulator2())
    fmt.Println(accumulator2())
    fmt.Println(accumulator2())
    fmt.Printf("%p\n", &accumulator2)
}
