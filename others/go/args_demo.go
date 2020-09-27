package main

import "fmt"


// 可变参数
func f(args ...int){
    for _, arg := range args {
        fmt.Println(arg)
    }
    fmt.Println(args)
}

func main() {

    f(1,2,3)
    f(4,5)
    f(6)

}

