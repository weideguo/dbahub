package main
import (
    "bufio"
    "fmt"
    "io"
    "os"
)
func main() {
    file, err := os.Open("./output.txt")
    if err != nil {
        fmt.Println("open file failed= ", err)
    }
    defer file.Close()
    reader := bufio.NewReader(file)
    for {
        str, err := reader.ReadString('\n') //读到一个换行就结束
        if err == io.EOF {                  //io.EOF 表示文件的末尾
            break
        }
        fmt.Print(str)
    }
    fmt.Println("end read")
}
