package main
import (
    "fmt"
)
func main() {
    str := "Hello HaiCoder!"
    fmt.Println(string(str[:len(str)-1]))
    fmt.Println(string(str[len(str)-1]))
}
