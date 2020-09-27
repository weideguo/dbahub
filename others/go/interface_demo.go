package main
import (
    "fmt"
)

// 定义一个数据写入器
type DataWriter interface {
    //WriteData(data interface{}) error
    WriteData(data string) error
}

// 定义文件结构，用于实现DataWriter
type file struct {
}

// 实现DataWriter接口的WriteData方法
//func (d *file) WriteData(data interface{}) error {
func (d *file) WriteData(data string) error {
    // 模拟写入数据
    fmt.Println("WriteData:", data)
    return nil
}

func main() {
    // 实例化file
    f := new(file)
    
    // 不使用接口
    f.WriteData("data not use interface")    

    // 使用接口
    var writer DataWriter
    writer = f
    // 使用DataWriter接口进行数据写入
    writer.WriteData("data use interface")
}
