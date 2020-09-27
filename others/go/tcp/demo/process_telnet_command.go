package main
import (
    "fmt"
    "strings"
)
/*
@close @shutdown 是telnet内部命令，使用telnet客户端时对客户端天然生效
*/

func processTelnetCommand(str string, exitChan chan int) bool {
    if strings.HasPrefix(str, "@close") {
        // @close指令表示终止本次会话
        fmt.Println("Session closed")
        return false
        
    } else if strings.HasPrefix(str, "@shutdown") {
        // @shutdown指令表示终止服务进程
        fmt.Println("Server shutdown")
        exitChan <- 0
        return false
    }
    
    fmt.Println(str)
    return true
}
