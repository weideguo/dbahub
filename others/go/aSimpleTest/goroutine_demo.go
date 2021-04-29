package main
import (
    "fmt"
    "time"
)
func running() {
    var times int
    // 构建一个无限循环
    for {
        times++
        fmt.Println("tick", times)
        // 延时1秒
        time.Sleep(time.Second)
    }
}

/*
多线程程序在单核心的 cpu 上运行，称为并发；多线程程序在多核心的 cpu 上运行，称为并行。并发主要由切换时间片来实现“同时”运行。
并发（concurrency）：把任务在不同的时间点交给处理器进行处理。在同一时间点，任务并不会同时运行。
并行（parallelism）：把每一个任务分配给每一个处理器独立完成。在同一时间点，任务一定是同时运行。

*/

func main() {
    go running()        //如果不使用并发 则后面的代码不会被运行
    
    // 接受命令行输入
    var input string
    fmt.Scanln(&input)  //阻塞至获取
    fmt.Println(input) 
    //默认退出时结束后台goroutine
}
