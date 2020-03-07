package main
import (
    "context"
    "fmt"
)
func main() {
    gen := func(ctx context.Context) <-chan int {
        dst := make(chan int)
        n := 1
        go func() {
            for {
                select {
                case <-ctx.Done():
                    fmt.Println("done")
                    return // return结束该goroutine，防止泄露
                case dst <- n:
                    fmt.Println("gen: ", n)
                    n++
                }
            }
        }()
        return dst
    }
    ctx, cancel := context.WithCancel(context.Background())
    defer cancel() // 当我们取完需要的整数后调用cancel
    for n := range gen(ctx) {
        fmt.Println(n)
        if n == 5 {
            break
        }
    }
}
/*
上下文
每个 goroutine 在执行之前，都要先知道程序当前的执行状态，通常将这些执行状态封装在一个 Context 变量中，传递给要执行的 goroutine 中
包含 goroutine 的运行状态、环境、现场等信息
用于并发控制和超时控制
*/
