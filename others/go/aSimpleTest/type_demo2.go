package main

import (
"fmt"
"encoding/json"
"unsafe"

"github.com/weideguo/goDemo/aSimpleTest/typedemo"
)

func NewDesc(FqName, help string, variableLabels []string ) *typedemo.Desc {
	d := &typedemo.Desc{
		FqName:         FqName,
	}
    
    return d

}



func main(){
    
    // descxx := &Desc{
	// 	fqName:         "xxx",
	// 	help:           "xxx",
	// 	variableLabels: []string{},
	// }
    
    desc := NewDesc("xxx","xxx",[]string{})
    
    // descxx.fqName = descxx.fqName+"aaa"
    
    // 第一个属性地址为结构体的地址
    var1 := desc
    v1 := (*string)(unsafe.Pointer(var1))
    *v1 = *v1+"a123v"
    // *v1 = "a123v"
    
    // 通过偏移量计算第二个属性的地址
    var2 := uintptr(unsafe.Pointer(desc)) + unsafe.Sizeof(string(""))
    v2 := (*string)(unsafe.Pointer(var2))
    
    label := map[string]string{"mysqlhost": "127.0.0.1:3306"}
    
    _label, _ := json.Marshal(label)

    *v2 = *v2+string(_label)
    
    
    
	fmt.Println(desc.FqName)
    fmt.Println(desc)
    
}

// 通过unsafe可以在外部修改私有属性的值
// 否则不能在外部修改与获取私有属性的值（即小写开头的属性）
