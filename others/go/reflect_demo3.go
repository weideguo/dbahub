package main

import (
    "fmt"
    "reflect"
)


func main() {
    
    type cat struct {
        Name string
        Type int `json:"type" id:"100"`     // 带有结构体tag的字段，用``或""包含
    }
    
    ins := cat{Name: "mimi", Type: 1}
    
    typeOfCat := reflect.TypeOf(ins)
    
    // 遍历结构体所有成员
    for i := 0; i < typeOfCat.NumField(); i++ {
        
        fieldType := typeOfCat.Field(i)
        //fmt.Printf(fieldType)
        fmt.Printf("name: %v  tag: '%v'\n", fieldType.Name, fieldType.Tag)
    }
    
    c1, isExist :=typeOfCat.FieldByName("Name")
    if isExist {
        fmt.Println(c1)
        fmt.Println(c1.Name)
        /*
        结构体成员的类型信息
            Name      string     // 字段名
            PkgPath   string     // 字段路径
            Type      Type       // 字段反射类型对象
            Tag       StructTag  // 字段的结构体标签
            Offset    uintptr    // 字段在结构体中的相对偏移
            Index     []int      // Type.FieldByIndex中的返回的索引值
            Anonymous bool       // 是否为匿名字段
        */     
    }    

    if catType, ok := typeOfCat.FieldByName("Type"); ok {
        fmt.Println(catType.Tag)
        fmt.Println(catType.Tag.Get("json"), catType.Tag.Get("id"))
    }
}
