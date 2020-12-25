package main

import (
	"fmt"
	"github.com/otiai10/gosseract/v2"
)

func main() {
	client := gosseract.NewClient()
	defer client.Close()
	client.SetImage("image.png")
	text, _ := client.Text()
	fmt.Println(text)
	// Hello, World!
}
/*
安装依赖
yum install tesseract tesseract-devel
go get -t github.com/otiai10/gosseract

设置文件
image.png
*/