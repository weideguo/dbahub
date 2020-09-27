package main

import (
    "fmt"
    "reflect"
)

type S1 interface{}

func f(age int, name S1) {
    fmt.Println(age,name)
}

func ff() {
    fmt.Println("ffff")
}

//inject 的实现样例
func main(){
    m := make(map[reflect.Type]reflect.Value)
    
    //构造map
    t := reflect.TypeOf( (*S1)(nil) )
    t = t.Elem()
    s := "nnnn"
    m[t]=reflect.ValueOf(s)
    
    v := 1233
    m[reflect.TypeOf(v)]=reflect.ValueOf(v)
    
    fmt.Println(m)


    type Staff struct {
        Name S1
        Age int
    }
    
    //注入结构体
    staff := Staff{}
    p := reflect.ValueOf(&staff)
    pv := p.Elem()    
    
    f0 :=pv.Field(0)
    setV := m[f0.Type()]    
    f0.Set(setV)
    
    f1 :=pv.Field(1)
    setV1 := m[f1.Type()]
    f1.Set(setV1)   
 
    fmt.Println(f0.Type(),f1.Type(),staff)



    //构建注入函数的参数
    ft := reflect.TypeOf(f)
    var in = make([]reflect.Value, ft.NumIn())
    fmt.Println(ft,ft.In(0),ft.In(1),in,ft.NumIn())

    in[0]=m[ft.In(0)]
    in[1]=m[ft.In(1)]

    fmt.Println(in)
    //通过反射调用函数
    reflect.ValueOf(f).Call(in)
    
    //调用无参函数 
    reflect.ValueOf(ff).Call(nil)
}
