package main

import (
    "fmt"
    "net"
)

func server(address string, exitChan chan int) {
    l, err := net.Listen("tcp", address)
    if err != nil {
        fmt.Println(err.Error())
        exitChan <- 1
    }
    fmt.Println("listen: " + address)
    defer l.Close()
    for {
        // 新连接没有到来时, Accept是阻塞的
        conn, err := l.Accept()
        if err != nil {
            fmt.Println(err.Error())
            continue
        }
        // 根据连接开启会话, 这个过程需要并行执行
        go handleSession(conn, exitChan)
    }
}
