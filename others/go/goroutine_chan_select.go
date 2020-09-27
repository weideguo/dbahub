package main

import (
    "fmt"
    "time"
)

func main(){
    start := time.Now()
    c := make(chan interface{})
    ch1 := make(chan int)
    ch2 := make(chan int)

    go func() {
        
        time.Sleep(5*time.Second)
        close(c)
    }()

    go func() {

        time.Sleep(3*time.Second)
        ch1 <- 3
    }()

    go func() {

        time.Sleep(3*time.Second)
        ch2 <- 5
    }()

    fmt.Println("Blocking on read...")
    
    // select语句会阻塞，直到监测到一个可以执行的IO操作为止。
    // 有default则不会阻塞
    select {
    // 每个 case 语句里必须是一个 IO 操作
    case <- c:

        fmt.Printf("Unblocked %v later.\n", time.Since(start))

    case <- ch1:

        fmt.Printf("ch1 case...\n")
    case <- ch2:

        fmt.Printf("ch2 case...\n")
    //default:

    //     fmt.Printf("default go...\n")
    }

}
