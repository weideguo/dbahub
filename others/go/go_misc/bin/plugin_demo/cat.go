package main

import "fmt"

type Cat struct{}

func (d Cat) Walk(a string, b int) {
    fmt.Println("cat walk", a, b)
}

func (c Cat) Meow(a string, b int) {
    fmt.Println("cat meow", a, b)
}
