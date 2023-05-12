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

type Scroll3 struct {
    Scroll2
    D string
}

func (s *Scroll) SetA(a int){
    s.A = a
}

func (s *Scroll) SetB(b string){
    s.B = b
}


func (s *Scroll2) SetB(b string){
    s.B = b+"22222"
}

func (s *Scroll2) SetC(c string){
    s.C = c
}

func (s *Scroll3) SetD(d string){
    s.D = d
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
    
    s3 := &Scroll3{}
    s3.SetA(1)
    s3.SetB("bbb3")
    s3.SetC("ccc3")
    s3.SetD("ddd3")
    fmt.Println(s1)
    fmt.Println(s2)
    fmt.Println(s3)
    fmt.Println(s3.A)
}