package main

import (
    "fmt"
    "time"
)

func main() {
    done := make(chan int)

    go func(){
        fmt.Println("你好, 世界")
        time.Sleep(3 * time.Second)
        //done <- 1               
        <- done                 //接收任意数据，忽略接收的数据
        //data := <- done       //阻塞接收数据
        //data, ok := <- done   //非阻塞接收数据
    }()

    done <- 1                   // main的goroutine 通过管道通知匿名goroutine
    //<- done
}
