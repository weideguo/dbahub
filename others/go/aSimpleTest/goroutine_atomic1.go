package main

import (
    "fmt"
    "sync"
    //"sync/atomic"
)

func main(){
    var wg sync.WaitGroup
    var x int32 = 0
    
    f := func(){
        defer wg.Done()
        //atomic.AddInt32(&x, 1)
        fmt.Println(x)
    }
    
        
    wg.Add(20)
    
    for i:=0;i<20;i++ {
        go f()
    }
    wg.Wait()
}
