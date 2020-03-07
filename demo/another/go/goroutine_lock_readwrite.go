package main
import (
    "sync"
    "time"
)
var m *sync.RWMutex
var wg sync.WaitGroup
func main() {
    m = new(sync.RWMutex)
    wg.Add(4)
    go write(1)
    go read(2)
    go read(3)
    go write(4)
    wg.Wait()
}
func read(i int) {
    println(i,"read start")
    m.RLock()
    println(i,"reading")
    time.Sleep(1*time.Second)
    m.RUnlock()
    println(i,"read over")
    wg.Done()
}
func write(i int) {
    println(i,"write start")
    m.Lock()
    println(i,"writing")
    time.Sleep(1*time.Second)
    m.Unlock()
    println(i,"write over")
    wg.Done()
}
/*
读写锁
读读 不互斥
读写 互斥
写写 互斥
操作的锁定和解锁分别是func (*RWMutex) Lock和func (*RWMutex) Unlock；
读操作的锁定和解锁分别是func (*RWMutex) Rlock和func (*RWMutex) RUnlock
*/
