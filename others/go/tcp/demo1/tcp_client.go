package main
import (
    "io"
    "log"
    "net"
    "os"
)
func main() {
    addr := "localhost:9000"
    if len(os.Args) >1 {
        addr = os.Args[1]
    }
  
    conn, err := net.Dial("tcp", addr)
    if err != nil {
        log.Fatal(err)
    }
    done := make(chan struct{})
    go func() {
        // 从连接或许消息发标准输出
        io.Copy(os.Stdout, conn)   
        log.Println("done")
        done <- struct{}{} // 向主Goroutine发出信号
    }()
    //无限循环从标准输入获取信息发送到连接
    mustCopy(conn, os.Stdin)
    conn.Close()
    <-done // 等待后台goroutine完成
}
func mustCopy(dst io.Writer, src io.Reader) {
    /*
    for {
        io.Copy(dst, src)
    }
    */
    
    if _, err := io.Copy(dst, src); err != nil {
        log.Fatal(err)
    }
    
}
