package main
import (
    "fmt"
    "runtime"
    "time"
    "sync"
)

//锁的使用

var counter int = 0
func Count(lock *sync.Mutex) {
    
    fmt.Println("begin: ",counter)
    time.Sleep(1*time.Second)
    lock.Lock()
    counter++
    fmt.Println("end: ",counter)
    lock.Unlock()
}
func main() {
    lock := &sync.Mutex{}
    for i := 0; i < 10; i++ {
        go Count(lock)
    }
    for {
        lock.Lock()
        c := counter
        lock.Unlock()
        fmt.Println("check")
        // 让出其他运行然后再执行下一步，否则将一直再次循环
        runtime.Gosched()
        if c >= 10 {
            break
        }
    }
    
    var x string
    fmt.Scanln(&x)
    fmt.Println("all done")
}
