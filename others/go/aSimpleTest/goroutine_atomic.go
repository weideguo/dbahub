package main
import (
    "fmt"
    "runtime"
    "sync"
    //"time"
    //"math/rand"
    "sync/atomic"
)
var (
    count int32
    wg    sync.WaitGroup
)

func main() {
    wg.Add(2)
    go incCount()
    go incCount()
    go incCount()
    wg.Wait()              //等待goroutine运行完毕
    fmt.Println(count)
}

func incCount() {
    defer wg.Done()
    for i := 0; i < 2; i++ {
        // 原子函数能够以很底层的加锁机制来同步访问整型变量和指针
        atomic.AddInt32(&count, 1)
        runtime.Gosched()
        /*
        value := count
        runtime.Gosched()
        value++            //没有加锁 会导致结果被覆盖
        count = value
        */
    }
    //time.Sleep(rand.Intn(3) * time.Second) 

    
    //wg.Done()            // defer wg.Done() 放在函数开始与此作用相同
}
