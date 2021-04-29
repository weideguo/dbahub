package main

import "fmt"
import "bytes"
//import "time"
//import "runtime"

func main() {
    fmt.Printf("hello, world\n")
    //fmt.Println([]int{3,0})
    // CPU数量
    //fmt.Println(runtime.NumCPU())
    /*
    i := 0
    for range time.Tick(1 * time.Second)  {
        i = i+1
        fmt.Println(i)
    }
    */

    var out bytes.Buffer
    fmt.Println(out)
    fmt.Fprintf(&out,"%v ", 1)
    fmt.Println(out)
    fmt.Fprintf(&out,"%v ", 2)
    fmt.Fprintf(&out,"%v ", 3)
    fmt.Fprintf(&out,"%v ", 4)
    fmt.Println(out.String())
    
    fmt.Println(`aaa`)
    fmt.Println(511/2)
}
