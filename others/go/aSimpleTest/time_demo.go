package main

import (
    "fmt"
    "time"
)

func main(){
    // s := time.Now()
    // time.Sleep(time.Second)
    // e :=time.Now()
    // delta := e.Sub(s)
    // fmt.Println(delta)
    
    // 每秒运行一次
    i :=0
    for range time.NewTicker(1 * time.Second).C {
        fmt.Println(i)
        i++
    }
}
