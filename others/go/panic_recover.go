package main
import (
    "fmt"
    "runtime"
)

func ProtectRun(entry func()) {
    
    defer func() {
        err := recover()
        //XXX.(type) 只能用于switch
        switch err.(type) {
        case runtime.Error:                     // 运行时错误
            fmt.Println("runtime error:", err)
        default:                                // 非运行时错误
            fmt.Println("error:", err)
        }
    }()
    entry()
}
func main() {
    fmt.Println("begin")
    // 
    ProtectRun(func() {
        fmt.Println("f1 begin")
        panic("error by manul")
        fmt.Println("f1 end")
    })
    
    
    ProtectRun(func() {
        fmt.Println("f2 begin")
        var a *int
        *a = 1
        fmt.Println("f2 end")
    })
    fmt.Println("all done")
}
