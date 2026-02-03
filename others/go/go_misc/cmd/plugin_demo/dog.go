package main

import "fmt"

type Dog struct{}

func (d Dog) Walk(a string, b int) {
    fmt.Println("dog walk", a, b)
}

func (d Dog) Bark(a string, b int) {
    fmt.Println("dog bark", a, b)
}
