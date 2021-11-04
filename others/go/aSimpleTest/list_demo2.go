package main

import "fmt"

func main() {

    dsns := []string{"weideguo:weideguo@(127.0.0.1:1039)/", ""}
        
    for _,v := range dsns {
        fmt.Println(v)
    } 

}
