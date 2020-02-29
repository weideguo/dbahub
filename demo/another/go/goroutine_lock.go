package main
import (
    "fmt"
    "runtime"
    "sync"
)
var (
    counter int64
    wg      sync.WaitGroup
    mutex   sync.Mutex
)
// 互斥锁
// 互斥锁用于在代码上创建一个临界区，保证同一时间只有一个 goroutine 可以执行这个临界代码。

func main() {
    wg.Add(2)
    go incCounter(1)
    go incCounter(2)
    wg.Wait()
    fmt.Println(counter)
}
func incCounter(id int) {
    defer wg.Done()
    for count := 0; count < 2; count++ {
        //同一时刻只允许一个goroutine进入这个临界区
        mutex.Lock()
        {
            value := counter
            runtime.Gosched()
            value++
            counter = value
        }
        mutex.Unlock() //释放锁，允许其他正在等待的goroutine进入临界区
    }
}
