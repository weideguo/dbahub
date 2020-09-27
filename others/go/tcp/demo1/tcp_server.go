package main
import (
    "bufio"
    "fmt"
    "log"
    "net"
)
func main() {
    addr := "localhost:9000"
    listener, err := net.Listen("tcp", addr)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("listen: ",addr)
    go broadcaster()
    for {
        conn, err := listener.Accept()
        if err != nil {
            log.Print(err)
            continue
        }
        go handleConn(conn)
    }
}
type client chan<- string // 对外发送消息的通道
var (
    entering = make(chan client)
    leaving  = make(chan client)
    messages = make(chan string) // 所有连接的客户端
)
func broadcaster() {
    clients := make(map[client]bool)
    for {
        select {
        case msg := <-messages:
            // 把所有接收到的消息广播给所有客户端
            // 发送消息通道
            for cli := range clients {
                cli <- msg
            }
        case cli := <-entering:
            clients[cli] = true
        case cli := <-leaving:
            delete(clients, cli)
            close(cli)
        }
    }
}
func handleConn(conn net.Conn) {
    ch := make(chan string)    // 对外发送客户消息的通道
    go clientWriter(conn, ch)  // 后台向客户端发消息   

    who := conn.RemoteAddr().String()
    ch <- "欢迎 " + who
    messages <- who + " 上线"
    entering <- ch
    
    input := bufio.NewScanner(conn)
    //无限循环阻塞式接收信息 
    for input.Scan() {
        messages <- who + ": " + input.Text()
        messages <- who + ": xxxxxx"
    }
    
    leaving <- ch
    messages <- who + " 下线"
    conn.Close()
}
func clientWriter(conn net.Conn, ch <-chan string) {
    for msg := range ch {
        //发送消息给客户端
        fmt.Fprintln(conn, msg) 
    }
}
