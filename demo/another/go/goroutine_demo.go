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
并发(Concurrency)和并行(Parallelism)


*/

func main() {
    go running()        //如果不适用并发 则后面的代码不会被同事运行
    
    // 接受命令行输入
    var input string
    fmt.Scanln(&input)  //阻塞至获取
    fmt.Println(input) 
    //默认退出时结束后台goroutine
}
