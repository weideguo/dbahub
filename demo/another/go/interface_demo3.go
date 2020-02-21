package main
import (
    "fmt"
)
func main() {
    //
    var x interface{}
    //x = nil 
    x = 10
    // 判断类型 正确则提取值 
    value, ok := x.(int)
    fmt.Println(value, ",", ok)
}
