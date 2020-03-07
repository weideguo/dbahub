package main
import (
    "fmt"
    "sync"
    "time"
)
var (
    counter int64
    //mutex   sync.RWMutex
    mutex   sync.Mutex
)
//Mutex 完全阻止进入代码区
//sync 包中的 RWMutex 提供了读写互斥锁的封装。
//比互斥锁更加高效,会阻止写，但不阻止读

func main() {
    c := make(chan int)
    go incCounter(1,c)
    go incCounter(2,c)
    <- c
    <- c
    fmt.Println(counter)
}
func incCounter(id int,c chan int) {
    for count := 0; count < 2; count++ {
        //同一时刻只允许一个goroutine进入这个临界区
        mutex.Lock()
        {
            value := counter
            time.Sleep(time.Second)
            value++
            counter = value
            fmt.Println(counter)
        }
        mutex.Unlock()   //释放锁，允许其他正在等待的goroutine进入临界区
    }
    c <- 1
}
