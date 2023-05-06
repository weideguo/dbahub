package main

import "fmt"

type Scroll struct {
    A int
    B string
}

// 实现继承
type Scroll2 struct {
    Scroll
    C string
}

func (s *Scroll) SetA(a int){
    s.A = a
}

func (s *Scroll) SetB(b string){
    s.B = b
}


func (s *Scroll2) SetC(c string){
    s.C = c
}

func main(){
    s1 := &Scroll{}
    s1.SetA(1)
    s1.SetB("bbb")
    // s1.SetC("ccc")   
    s2 := &Scroll2{}
    s2.SetA(1)
    s2.SetB("bbb2")
    s2.SetC("ccc")
    fmt.Println(s1)
    fmt.Println(s2)
}