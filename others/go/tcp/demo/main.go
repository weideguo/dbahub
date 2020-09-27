package main
import (
    "os"
)

/*
main 包多下的多个文件关联，编译时需要将多个文件同时放入
go build f1.go f2.go ... fn.go
*/

func main() {
    exitChan := make(chan int)
    go server("127.0.0.1:7001", exitChan)
    // 通道阻塞, 等待接收返回值
    code := <-exitChan
    // 标记程序返回值并退出
    os.Exit(code)
}
