package main

import (
    "fmt"
    "os"
    "sync"
    "time"
    "runtime"
)

type secret struct {
    RWM      sync.RWMutex
    M        sync.Mutex
    password string
}

// 通过rwmutex写
func Change(c *secret, pass string) {
    c.RWM.Lock()
    fmt.Println("Change with rwmutex lock", time.Now().Second())
    time.Sleep(3 * time.Second)
    c.password = pass
    c.RWM.Unlock()
}

func noMutexShow(c *secret) string {
    fmt.Println("show with no mutex",time.Now().Second())
    time.Sleep(1 * time.Second)
    return c.password
}

// 通过rwmutex读
func rwMutexShow(c *secret) string {
    c.RWM.RLock()
    fmt.Println("show with rwmutex",time.Now().Second())
    time.Sleep(1 * time.Second)
    defer c.RWM.RUnlock()
    return c.password
}

// 通过mutex读，和rwMutexShow的唯一区别在于锁的方式不同
func mutexShow(c *secret) string {
    c.M.Lock()
    fmt.Println("show with mutex:",time.Now().Second())
    time.Sleep(10 * time.Second)
    defer c.M.Unlock()
    return c.password
}

func main() {

    //使用的cpu核心
    // runtime.GOMAXPROCS(runtime.NumCPU())  //1.5默认使用
    runtime.GOMAXPROCS(1)

    var Password = secret{password: "myPassword"} 
    
    var show = func(c *secret) string { return "" }

    // 通过变量赋值的方式，选择并重写showFunc函数
    if len(os.Args) == 1 {
        fmt.Println("Using sync.RWMutex!",time.Now().Second())
        show = mutexShow
    } else if len(os.Args) == 2 {
        fmt.Println("Using sync.Mutex!",time.Now().Second())
        show = rwMutexShow
    } else {
        fmt.Println("Using no Mutex!",time.Now().Second())
        show = noMutexShow
    }
    
    var wg sync.WaitGroup

    // 激活5个goroutine，每个goroutine都查看
    // 根据选择的函数不同，showFunc()加锁的方式不同
    for i := 0; i < 5; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            fmt.Println("Go Pass:", show(&Password),time.Now().Second())
        }()
    }
    
    // 激活一个申请写锁的goroutine
    go func() {
        wg.Add(1)
        defer wg.Done()
        Change(&Password, "123456")
    }()
    // 阻塞，直到所有wg.Done
    wg.Wait()
}
