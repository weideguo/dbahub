package main

import (
    "fmt"
    "time"
    "sync"
)

func main() {
    var wg sync.WaitGroup
    wg.Add(2)
    // 带缓冲通道 发送时无需等待接收方接收即可完成发送过程，并且不会发生阻塞，只有当存储空间满时才会发生阻塞。
    ch := make(chan int, 3)
    // 无缓冲通道 发送接收相互等待
    //ch := make(chan int)
    fmt.Println(len(ch))
    go func(){
        defer wg.Done()
        for i:=1;i<6;i++ {
            ch <- i
            fmt.Println("put ",i)
            time.Sleep(time.Second)
        }
    }()

    go func(){
        defer wg.Done()
        for i:=1;i<6;i++ {
            time.Sleep(5 * time.Second)
            fmt.Println("get ",<- ch)
        }
    }()
    wg.Wait()
}
