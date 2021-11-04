package main

import (
    "fmt"
    "strings"
)

func main() {
    str := " aa bb cc    "
    s := strings.Trim(str," ")
    fmt.Println("||"+s+"||")
    fmt.Println(len(s))


    dsn := "aa bb cc , dd ee dd "    
    dsns := strings.Split(dsn, ",")
    fmt.Println(dsns)

    for k, v := range dsns {
        dsns[k] = strings.Trim(v, " ")
    }

    fmt.Println(dsns)

}
