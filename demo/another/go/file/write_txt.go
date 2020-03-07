package main
import (
    "bufio"
    "fmt"
    "os"
)
func main() {
    filePath := "./output.txt"
    
    file, err := os.OpenFile(filePath, os.O_WRONLY|os.O_CREATE, 0666)
    //file, err := os.OpenFile(filePath, os.O_WRONLY, 0666)
    if err != nil {
        fmt.Printf("open file failed= %v \n", err)
        return
    }
    defer file.Close()
    
    writer := bufio.NewWriter(file)
    
    str := "wwwww\n"
    writer.WriteString(str)
    str = "bbbb\n"
    writer.WriteString(str)
    //因为 writer 是带缓存的，因此在调用 WriterString 方法时，内容是先写入缓存的
    //所以要调用 flush方法，将缓存的数据真正写入到文件中。
    writer.Flush()
}

/*
    // Exactly one of O_RDONLY, O_WRONLY, or O_RDWR must be specified.
    O_RDONLY int = syscall.O_RDONLY // open the file read-only.
    O_WRONLY int = syscall.O_WRONLY // open the file write-only.
    O_RDWR   int = syscall.O_RDWR   // open the file read-write.
    // The remaining values may be or'ed in to control behavior.
    O_APPEND int = syscall.O_APPEND // append data to the file when writing.
    O_CREATE int = syscall.O_CREAT  // create a new file if none exists.
    O_EXCL   int = syscall.O_EXCL   // used with O_CREATE, file must not exist.
    O_SYNC   int = syscall.O_SYNC   // open for synchronous I/O.
    O_TRUNC  int = syscall.O_TRUNC  // truncate regular writable file when opened.
*/
