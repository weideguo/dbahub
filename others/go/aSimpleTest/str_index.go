package main

import (
    "fmt"
    "strings"
)

func main() {
    str := "hello world"
    index1 := strings.Index(str, "world")
    index2 := strings.Index(str, "worldx")
    index3 := strings.Index(str, "hello")
    fmt.Println(index1)
    fmt.Println(index2)
    fmt.Println(index3)
}
