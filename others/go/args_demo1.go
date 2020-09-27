package main

import "fmt"
import "os"

func main() {
    // 用于接受执行时传入的参数
    // go run xxx.go arg1 arg2 arg3
    fmt.Println(os.Args)
}
