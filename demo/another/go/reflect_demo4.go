package main
import (
    "fmt"
    "reflect"
)

// 定义结构体
type dummy struct {
    a int
    b string
    // 嵌入字段
    float32
    bool
    next *dummy
}

func main() {
    // 值包装结构体
    d := reflect.ValueOf(dummy{
            a: 100,
            next: &dummy{},
    })
    // 获取字段数量
    fmt.Println(d.NumField())
    // 输出字段类型
    fmt.Println(d.Field(2).Type())
    // 根据名字查找字段
    fmt.Println(d.FieldByName("a").Int())
    fmt.Println(d.FieldByName("b").Type())
    // 根据索引查找值中, next字段的int字段的值
    // 嵌套成员使用数组访问
    fmt.Println(d.FieldByIndex([]int{4}))
    fmt.Println(d.FieldByIndex([]int{4,0}))
}
