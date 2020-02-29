package main

import (
    "fmt"
    "time"
)

var c chan int

func waiting(w string, sec int) {

    time.Sleep(time.Duration(sec) * time.Second)
    fmt.Println(w, "is ready")
    c <- 1
}


func main() {
    c = make(chan int)
    go waiting("coffee", 1)
    go waiting("tea1", 2)
    go waiting("tea2", 3)
    go waiting("tea3", 4)
    go waiting("tea4", 5)
    go waiting("tea5", 6)
    go waiting("tea6", 7)
    fmt.Println("I,am waiting")
    //time.Sleep(3 * time.Second)
    i := 0
L:
    for {
        select {
        case <-c:
            i++
            if i > 6 {
                // 终止并进入到哪
                break L 
            }
        }
    }
    fmt.Println("end")
}
