package main

import (   
    "fmt"
    "strconv"
)

func main() {
    a := 3.1234
    
    var b float64
    b=3.12343140591274914
    
    fmt.Println(a)
    fmt.Println(b)
    fmt.Println(fmt.Sprintf("%f",b))
    fmt.Println(strconv.FormatFloat(b, 'f', -1, 64))
}