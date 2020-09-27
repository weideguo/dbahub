package main 

import (
    "fmt"
    "reflect"
)

/*
反射是指在程序运行期对程序本身进行访问和修改的能力。
动态类型语言没有反射 
C/C++ 语言没有支持反射功能;  JAVA C# go支持完整的反射功能
*/

func main(){
    var x int = 10
    v := reflect.TypeOf(x)
    fmt.Println(v.Kind())
    fmt.Println(v.Name())
    
    y :="100"
    a,b := reflect.TypeOf(y),reflect.ValueOf(y)
    m :=make(map[reflect.Type]reflect.Value)    
    m[a]=b
    fmt.Println(a,b,m)    
}
