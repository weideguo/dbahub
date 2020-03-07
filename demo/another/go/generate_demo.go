package main

import "fmt"

//go:generate go run generate_demo.go
//go:generate go version
func main() {
	fmt.Println("http://c.biancheng.net/golang/")
}

/*
运行
go generate generate_demo.go

执行文件中的 //go:generate的注释后的命令
*/

