package main

import "fmt"

func DCall(){
    fmt.Println("plugin.so was called") 
}

func DCallWithParam(msg string){
    fmt.Println("function with param: ",msg) 
}

func DCallWithReturn(msg string)(string){
    fmt.Println("function with return: ",msg)
    return msg
}

func main() {
    fmt.Println("go plugin demo done")
}

/*
编译成动态库xxx.so
go build --buildmode=plugin plugin.go
*/
