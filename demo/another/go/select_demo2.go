


package main

import "fmt"

var ch1 chan int
var ch2 chan int
var chs = []chan int{ch1, ch2}
var numbers = []int{1, 2, 3, 4, 5}

func getNumber(i int) int {
    fmt.Printf("numbers[%d]\n", i)

    return numbers[i]
}
func getChan(i int) chan int {
    fmt.Printf("chs[%d]\n", i)

    return chs[i]
}

func main () {

    // 所有channel表达式都会被求值、所有被发送的表达式都会被求值。
    // 自上而下、从左到右
    select {
    case getChan(0) <- getNumber(2):
    //case  chs[0] <- 1 :
        fmt.Println("1th case is selected.")
    case getChan(1) <- getNumber(3):

        fmt.Println("2th case is selected.")
    default:

        fmt.Println("default!.")
    }
}

