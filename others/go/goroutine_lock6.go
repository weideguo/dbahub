package main

import (
    "fmt"
    "runtime"
    "sync"
    "time"
)

//饥饿

func main() {
    runtime.GOMAXPROCS(3)

    var wg sync.WaitGroup
    const runtime = 1 * time.Second
    var sharedLock sync.Mutex

    greedyWorker := func() {
        defer wg.Done()
        var count int
        for begin := time.Now(); time.Since(begin) <= runtime; {
            sharedLock.Lock()
            time.Sleep(3 * time.Nanosecond)
            sharedLock.Unlock()
            count++
        }

        fmt.Printf("Greedy worker was able to execute %v work loops\n", count)
    }

    politeWorker := func() {
        defer wg.Done()
        var count int
        for begin := time.Now(); time.Since(begin) <= runtime; {
            sharedLock.Lock()
            time.Sleep(1 * time.Nanosecond)
            sharedLock.Unlock()

            sharedLock.Lock()
            time.Sleep(1 * time.Nanosecond)
            sharedLock.Unlock()

            sharedLock.Lock()
            time.Sleep(1 * time.Nanosecond)
            sharedLock.Unlock()
            count++
        }
        fmt.Printf("Polite worker was able to execute %v work loops\n", count)
    }

    wg.Add(2)
    go greedyWorker()
    go politeWorker()

    wg.Wait()
}
