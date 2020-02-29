package main

import (
    "fmt"
    "reflect"
)


func main(){
    x := 2                      // value type variable?
    a := reflect.ValueOf(2)     // 2 int no
    b := reflect.ValueOf(x)     // 2 int no
    c := reflect.ValueOf(&x)    // &x *int no
    
    d := c.Elem()               // 2 int yes (x)
    
    //一个变量就是一个可寻址的内存空间，里面存储了一个值，并且存储的值可以通过内存地址来更新。
    //判断其是否可以被取地址
    fmt.Println(a.CanAddr()) 
    fmt.Println(b.CanAddr()) 
    fmt.Println(c.CanAddr()) 
    fmt.Println(d.CanAddr())
    fmt.Printf("%x \n",d.Addr())      //但不可以可以通过&取地址
    fmt.Printf("%x \n",&x)

    fmt.Printf("%v \n",d.CanSet())
    d.SetInt(100)
    fmt.Println(x)    

    /*
    反射值对象的判定及获取元素的方法
    Elem() Value    取值指向的元素值。类似于语言层*操作。
    Addr() Value    对可寻址的值返回其地址。类似于语言层&操作。
    CanAddr() bool  表示值是否可寻址
    CanSet() bool   返回值能否被修改。要求值可寻址且是导出的字段
    */
    /*
    反射值对象修改值的方法
    Setlnt(x int64)
    SetUint(x uint64)
    SetFloat(x float64)
    SetBool(x bool)
    SetBytes(x []byte)
    SetString(x string)
    */
}
