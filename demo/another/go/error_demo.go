package main

import (
    "fmt"
    "errors"
)

func f1(v int)(int,error){
    //基本用法
    if v < 0 {
        return -1, errors.New("math: some wrong catch in here")
    } else {
        return v,nil
    }
}


////////////////////////////////////////////////
//自定义错误
type dualError struct {
    Num     int
    problem string
} 

func (e dualError) Error() string {
    return fmt.Sprintf("\"%d\" is catched", e.Num)
}
func f2(v int)(int,error){
    if v < 0 {
        return -1, dualError{Num: v}
    } else {
        return v,nil
    }
} 
///////////////////////////////////////////////


func main(){
    a,err := f1(-100)
    if err != nil{
        fmt.Println(err)    
    } else {
        fmt.Println(a)
    }

    b,err2 := f2(-13)
    if err2 != nil{
        fmt.Println(err2)
    } else {
        fmt.Println(b)
    }
}
