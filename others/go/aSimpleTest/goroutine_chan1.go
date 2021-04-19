package main

import "fmt"

func channel_demo() {
    
    // 通道 可以用于go协程(goroutine)之间通信
    // var 通道变量 chan 通道类型
    // c := make(chan int)      //只能插入int
    // c := make(chan string)   //只能插入string
    c := make(chan interface{}) //可以插入任意类型
    
    /*
    //匿名函数创建goroutine
    
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

func fff(){ fmt.Println("xxx") }

// func fx(c chan int) {
func fx(c chan interface{}) {
    //var x interface{} =5
    c <- 5
    c <- "aa"
    c <- fff
    close(c)
}

func main(){
    channel_demo()
}
