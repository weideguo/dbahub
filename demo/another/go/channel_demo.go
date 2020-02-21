package main

import "fmt"

func channel_demo() {
    
    // 通道 可以用于go协程(goroutine)之间通信
    c := make(chan int)
    
    /*
    匿名函数创建goroutine
    
    go func() {
        c <- 1
        c <- 3
        c <- 5
        close(c)
    }()
    */
    
    // goroutine
    go fx(c)

    for v := range c {
        fmt.Println(v)
    }
}

func fx(c chan int) {
    c <- 2
    c <- 4
    c <- 6
    close(c)
}

func main(){
    channel_demo()
}
