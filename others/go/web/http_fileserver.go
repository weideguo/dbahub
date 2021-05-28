package main

import (
    "fmt"
	"net/http"
)

func main() {

	http.Handle("/", http.FileServer(http.Dir(".")))     // 静态web服务器   
    fmt.Println("listen on :8081")
	http.ListenAndServe(":8081", nil)
}