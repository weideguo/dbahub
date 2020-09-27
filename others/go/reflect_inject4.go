package main

import (
    "fmt"
    "reflect"
)

func foo(v int) {
    fmt.Println(v)
}

func foo1(v int,b string) {
    fmt.Println(v, b)
}

func main(){

    v := reflect.ValueOf(foo)
    v.Call([]reflect.Value{reflect.ValueOf(2)})

    v1 := reflect.ValueOf(foo1)
    v1.Call([]reflect.Value{reflect.ValueOf(2),reflect.ValueOf("bbb")})
}
