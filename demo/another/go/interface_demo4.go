package main
import (
    "./p1"
    "fmt"
)

// 声明一个设备结构
type device struct {
}

// 实现io.Writer的Write()方法
func (d *device) Write(p []byte) (n int, err error) {
    fmt.Println("write function")
    return 0, nil
}

// 实现io.Closer的Close()方法
func (d *device) Close() error {
    fmt.Println("close function")
    return nil
}

func main() {
    // 声明写入关闭器, 并赋予device的实例
    var wc io.WriteCloser = new(device)
    
    wc.Write(nil)
    wc.Close()


    // 声明写入器, 并赋予device的新实例
    var writeOnly io.Writer = new(device)     //只修剪获取到符合接口的属性 
    // writeOnly := new(device)               //能获取获取到完整的属性
    writeOnly.Write(nil)
    // writeOnly.Close()  //io.Writer并没有这个方法 因而调用会失败
}
