package main
import (
    "bufio"
    "fmt"
    "net"
    "strings"
)

func handleSession(conn net.Conn, exitChan chan int) {
    fmt.Println("Session started:")
    // 创建一个网络连接数据的读取器
    reader := bufio.NewReader(conn)
    for {
        // 读取字符串, 直到碰到回车返回
        str, err := reader.ReadString('\n')
        if err == nil {
            // 去掉字符串尾部的回车
            str = strings.TrimSpace(str)
            // 处理Telnet指令
            if !processTelnetCommand(str, exitChan) {
                conn.Close()
                break
            }
            
            // 给客户端传数据
            conn.Write([]byte(str + "\r\n"))
            //另一种发送方式
            //fmt.Fprintln(conn, "hhhhh\r\n") 
        } else {
            // 发生错误
            fmt.Println("Session closed")
            conn.Close()
            break
        }
    }
}
