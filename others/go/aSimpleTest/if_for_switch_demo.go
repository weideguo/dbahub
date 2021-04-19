package main

import "fmt"

func if_demo(a int, b int){

    if a>b {
        fmt.Printf("yes")
    } else {
        fmt.Printf("no")
    }

}


func for_demo(a int) {
    for i := 0; i < a; i++ {
        fmt.Println(i)
        if i > 10 {
            break
        }
    }


}

func for_demo2() {
    var i int
    for {
        fmt.Println(i)
        if i > 10 {
            break
        }
        i++
    }

}


func for_demo3() {
    var i int
    for i <= 10 {
        fmt.Println(i)
        i++
    }

}

func switch_demo() {
    var a = "hello"
    switch a {
    case "hello":
        fmt.Println(1)
    case "world":
        fmt.Println(2)
    default:
        fmt.Println(0)
    }

}

func switch_demo2() {
    var r int = 111
    switch {
    case r > 10 && r < 20:
        fmt.Println(r)
    default:
        fmt.Println(0)
    }

}



func main() {
    // if_demo(2,1)
    // for_demo(20)
    // for_demo2()
    // for_demo3()
    // switch_demo()
    switch_demo2()
}
