package main
import (
    "fmt"
    "reflect"
)
func new_demo() {
    var a int =100
    // 取变量a的反射类型对象
    typeOfA := reflect.TypeOf(a)
    // 根据反射类型对象创建类型实例
    aIns := reflect.New(typeOfA)
    // 输出Value的类型和种类
    fmt.Println(a, aIns, aIns.Type(), aIns.Kind())
}

func add(a, b int) int {
    return a + b
}


func func_demo(){
    // 将函数包装为反射值对象
    funcValue := reflect.ValueOf(add)
    
    // 构造函数参数, 传入两个整型值 必须通过此构造参数
    paramList := []reflect.Value{reflect.ValueOf(10), reflect.ValueOf(20)}
    fmt.Println(paramList)    

    fmt.Println(funcValue)
    // 反射调用函数
    retList := funcValue.Call(paramList)
    // 获取第一个返回值, 取整数值
    fmt.Println(retList[0].Int())    
    fmt.Println(retList)    

}

func main(){
    //new_demo()
    func_demo()
}

