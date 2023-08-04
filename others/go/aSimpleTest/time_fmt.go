package main
import (
    "fmt"
    "time"
)

func main() {
    now := time.Now()
    //x := fmt.Sprintf("logs/%s-%s.log", now.Format("2006-01-02"), now.Format("150405") )
    x := fmt.Sprintf("logs/%s.log", now.Format("2006-01-02-150405"))
    fmt.Println(x)
}
