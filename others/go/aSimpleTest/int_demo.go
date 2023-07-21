package main

import (
    "fmt"
    "strconv"
)

func main() {
    hexStr := "A3" // 十六进制字符串
    decInt, err := strconv.ParseInt(hexStr, 16, 10) // 将十六进制字符串转换为十进制整数
    if err != nil {
        fmt.Println("解析十六进制字符串出错：", err)
        return
    }
    fmt.Printf("十六进制数 %s 转换为十进制数为 %d\n", hexStr, decInt)
}
