package main
import (
    "fmt"
    "reflect"
)

func type_ref(){
    type cat struct {
    }
    
    // typeOfCat := reflect.TypeOf(*&cat{})
    typeOfCat := reflect.TypeOf(cat{})
    fmt.Println(typeOfCat, typeOfCat.Name(), typeOfCat.Kind())         //通过反射获取类型信息

}

func type_ref2(){
    type cat struct {
    }

    typeOfCat := reflect.TypeOf(&cat{})
    fmt.Println(typeOfCat, typeOfCat.Name(), typeOfCat.Kind())   //反射类型对象的名称和种类 Go语言的反射中对所有指针变量的种类都是 Ptr 
    // 取过程被称为取元素，等效于对指针类型变量做了一个*操作，但不能进行*操作
    // 取指针类型的元素类型 不可以通过一个非指针类型获取它的指针类型 
    typeOfCat = typeOfCat.Elem()                                 
    fmt.Println(typeOfCat, typeOfCat.Name(), typeOfCat.Kind())   //反射类型对象的名称和种类
}

func comm_ref(){
    var x float64 = 3.4
    x = 100.1
    p := reflect.ValueOf(&x)       //获取到x的地址
    v := p.Elem()
    v.SetFloat(7.1)
    
    //fmt.Println(p)
    fmt.Println(v) 
    fmt.Println(v.Interface())
    fmt.Println(x)
}

func value_ref(){

    var a int = 1024
    valueOfA := reflect.ValueOf(a)
    fmt.Println(valueOfA.Interface())             //将值以 interface{} 类型返回，可以通过类型断言转换为指定类型
    var getA int = valueOfA.Interface().(int)
    var getA2 int = int(valueOfA.Int())

    fmt.Println(getA, getA2)
}

func struct_ref() {
    type T struct {
        A int
        B string
    }
    t := T{1, "skidoo"}
    fmt.Println("t is: ", t)
    //fmt.Println("t is: ", t.A)
    
    s := reflect.ValueOf(&t).Elem()
    s.Field(0).SetInt(11)
    s.Field(1).SetString("sss")
    fmt.Println("s is now: ", s)
    fmt.Println("s field: ", s.Field(1))
    fmt.Println("t is now: ", t)
    
    t.A=22
    t.B="xxx"
    fmt.Println("t is now: ", t)
}

func main(){
    //type_ref()
    //type_ref2()
    value_ref()
    //comm_ref()
    //struct_ref()
}
