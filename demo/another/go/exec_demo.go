package main

import (
    "fmt"
    "bytes"
    "os/exec"
)

func main(){
    //获取命令的路径
    //f, err := exec.LookPath("who")
    //cmd := exec.Command("whoami")
    cmd := exec.Command("echo","xxx")
    
    var outInfo bytes.Buffer
    //使用操作系统的标准输出
    //cmd.Stdout = os.Stdout
    cmd.Stdout = &outInfo
    
    var errInfo bytes.Buffer    
    cmd.Stderr = &errInfo

    //阻塞运行
    //cmd.Run()
    
    //非阻塞运行
    cmd.Start()
    //阻塞运行 阻塞等待结果
    cmd.Wait()    
    
    fmt.Println("OUT: ", outInfo.String())
    fmt.Println("ERR: ", errInfo.String())

}
