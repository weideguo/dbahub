package main

import "fmt"

type X struct{
    XX string

}

var (
yy X
)

func setYY(a string) {
    yy = X{a}

}


func main() {
    //x := X{"xxxx"}
    setYY("bbbb")

    fmt.Println(yy)

}
