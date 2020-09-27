package main

import (
    "fmt"
    "time"
)

func main(){
    s := time.Now()
    time.Sleep(time.Second)
    e :=time.Now()
    delta := e.Sub(s)
    fmt.Println(delta)
}
