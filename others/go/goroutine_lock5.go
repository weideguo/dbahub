package main

import (
    "bytes"
    "fmt"
    "runtime"
    "sync"
    "sync/atomic"
    "time"
)

//活锁有可能自行解开,死锁则不能

func main() {
    runtime.GOMAXPROCS(3)
    cv := sync.NewCond(&sync.Mutex{})
    go func() {
        for range time.Tick(1 * time.Second) { // 通过tick控制两个人的步调
            cv.Broadcast()
        }
    }()

    takeStep := func() {
        cv.L.Lock()
        cv.Wait()
        cv.L.Unlock()
    }

    tryDir := func(dirName string, dir *int32, out *bytes.Buffer) bool {
        fmt.Fprintf(out, " %+v", dirName)
        atomic.AddInt32(dir, 1)
        takeStep()                      //走上一步
        fmt.Println(dirName, *dir, *out)
        if atomic.LoadInt32(dir) == 1 { //走成功就返回
            fmt.Fprint(out, ". Success!")
            return true
        }
        takeStep() // 没走成功，再走回来
        atomic.AddInt32(dir, -1)
        fmt.Println(dirName, *dir, *out)
        return false
    }

    var left, right int32
    tryLeft := func(out *bytes.Buffer) bool {
        return tryDir("向左走", &left, out)
    }

    tryRight := func(out *bytes.Buffer) bool {
        return tryDir("向右走", &right, out)
    }

    walk := func(walking *sync.WaitGroup, name string) {
        var out bytes.Buffer
        defer walking.Done()
        defer func() { fmt.Println(out.String()) }()
        fmt.Fprintf(&out, "%v is trying to scoot:", name)

        fmt.Println(out)
        
        for i := 0; i < 5; i++ {
            if tryLeft(&out) || tryRight(&out) {
                return
            }
        }
        fmt.Fprintf(&out, "\n%v is tried!", name)
    }

    var trail sync.WaitGroup
    trail.Add(2)
    go walk(&trail, "男人") // 男人在路上走
    go walk(&trail, "女人") // 女人在路上走
    trail.Wait()
}
