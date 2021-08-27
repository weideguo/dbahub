package main

import (
    "fmt"
    "reflect"
)


type Person struct {
    Name        string `label:"Name is: "`
    Age         int    `label:"Age is: "`
    Gender      string `label:"Gender is: " default:"unknown"`
}
/*
tag格式
`key01:"value01" key02:"value02" key03:"value03"`
主要用于自定义的解析
使用json库解析时要遵循json库的tag格式
*/

func Print(obj interface{}) error {
    // 取 Value
    v := reflect.ValueOf(obj)

    // 解析字段
    for i := 0; i < v.NumField(); i++ {

        // 取tag
        field := v.Type().Field(i)
        tag := field.Tag

        // 解析label 和 default
        label := tag.Get("label")
        defaultValue := tag.Get("default")

        value := fmt.Sprintf("%v", v.Field(i))
        if value == "" {
            // 如果没有指定值，则用默认值替代
            value = defaultValue
        }

        fmt.Println(label + value)
    }

    return nil
}

func main() {
    person := Person{
        Name:  "xxx",
        Age:   29,
    }

    Print(person)

}
