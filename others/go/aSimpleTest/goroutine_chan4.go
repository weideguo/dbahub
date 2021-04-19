package main
import "fmt"
func main() {
    ch := make(chan int, 2)
   
    ch <- 0
    //ch <- 1
   
    close(ch)  //带缓冲通道的数据不会被释放，通道也没有消失。
    
    fmt.Println(cap(ch),len(ch))

    for i := 0; i < 4; i++ {
   
        v, ok := <-ch  //带缓冲通道关闭后将会获取通道类型的零值，然后停止阻塞并返回。
       
        fmt.Println(v, ok)
    }
}
