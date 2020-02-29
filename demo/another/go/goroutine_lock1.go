package main
import (
    "fmt"
    "sync"
)

var (
    count int
    countGuard sync.RWMutex    //读写锁
)



func GetCount() int {
    // 锁定
    countGuard.RLock()
    // 在函数退出时解除锁定
    defer countGuard.RUnlock()
    return count
}

func SetCount(c int) {
    countGuard.Lock()
    count = c
    countGuard.Unlock()
}

func main() {
    go SetCount(1)
    fmt.Println(GetCount())
}
