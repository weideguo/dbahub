package main

import (
    "fmt"
    //"reflect"
)


type Person struct {
    Name string    `json:"name"`
    Age  int       `json:"age" valid:"1-100"`
}

type Personx struct {
    Person
    Nxx string    `json:"nxx"`
}
  
 
func main() {
    p1 := Person{
        Name:  "xxx",
        Age:   29,
    }
    p := Personx{
        Person: p1,
        Nxx:  "xxx",
    }
    //v := reflect.ValueOf(p)
    //tag := v.Type().Field(3).Tag.Get("json")
    //fmt.Println(tag)
    fmt.Println(p)
}