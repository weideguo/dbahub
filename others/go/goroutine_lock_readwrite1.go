package main
import (
    "fmt"
    "sync"
    "time"
)
var (
    seq int64
    counter int64
    mutex   sync.RWMutex
    //mutex   sync.Mutex
)
/*
sync 包中的 RWMutex 提供了读写互斥锁的封装。
比互斥锁更加高效,会阻止写，但不阻止读
RWMutex是基于Mutex的，在Mutex的基础之上增加了读、写的信号量，并使用了类似引用计数的读锁数量
读锁与读锁兼容，读锁与写锁互斥，写锁与写锁互斥
*/
/*
type RWMutex struct {
    w           Mutex  // held if there are pending writers
    writerSem   uint32 // 写锁需要等待读锁释放的信号量
    readerSem   uint32 // 读锁需要等待写锁释放的信号量
    readerCount int32  // 读锁后面挂起了多少个写锁申请
    readerWait  int32  // 已释放了多少个读锁
}
*/


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
        //允许多个goroutine读 
        //只运行一个获得锁的goroutine写
        mutex.RLock()         //RWMutex读锁
        //mutex.Lock()        //RWMutex写锁 个方法跟Mutex类似
        {
            fmt.Println(id, "read0: ",counter)
            time.Sleep(time.Second)
            fmt.Println(id, "read1: ",counter)
            counter++
            fmt.Println(id, "write0:",counter)
            time.Sleep(time.Second)
            counter++
            fmt.Println(id, "write1:",counter)
            // counter = value
            // fmt.Println(counter)
        }
        mutex.RUnlock() 
        //mutex.Unlock() 
    }
    c <- 1
}

