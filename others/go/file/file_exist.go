package main
import (
    "fmt"
    "os"
)
func main() {
    // filename := "./file_exist.go"
    filename := os.Args[1] 
    
    a, err := os.Stat(filename)
    fmt.Println(a)
    fmt.Println(err)
    // 通过错误输出判断文件是否存在，即没有错误输出则文件存在，有错误输出则文件不存在
    fmt.Println(!os.IsNotExist(err))

}
