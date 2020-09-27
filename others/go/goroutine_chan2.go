package main

import (
    "fmt"
    "time"
)

func main(){
    timer := time.NewTimer(time.Second)
    /*
    // Timer 定义
    type Timer struct {
        C <-chan Time
        r runtimeTimer
    }
    */
    t := <- timer.C
    // timer.C <- 4 // C是一个只读的单向通道 不能写
    fmt.Println(t)

}
