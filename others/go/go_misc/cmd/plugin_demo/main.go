package main

import (
    "fmt"
    "reflect"
)

func SafeCallMethodWithArgs(obj interface{}, methodName string, args ...interface{}) {
    v := reflect.ValueOf(obj)
    if v.Kind() == reflect.Ptr && v.IsNil() {
        fmt.Println("对象为 nil")
        return
    }
    if v.Kind() != reflect.Ptr && v.CanAddr() {
        v = v.Addr()
    }

    method := v.MethodByName(methodName)
    if !method.IsValid() {
        fmt.Printf("方法 %s 未实现\n", methodName)
        return
    }

    // 转换参数
    in := make([]reflect.Value, len(args))
    for i, arg := range args {
        in[i] = reflect.ValueOf(arg)
    }

    method.Call(in)
}

func main() {
    var pet any

    pet = Dog{}
    SafeCallMethodWithArgs(pet, "Walk", "aaa", 111)
    SafeCallMethodWithArgs(pet, "Bark", "aaa", 111)
    SafeCallMethodWithArgs(pet, "Meow", "aaa", 111)

    pet = Cat{}
    SafeCallMethodWithArgs(pet, "Walk", "aaa", 111)
    SafeCallMethodWithArgs(pet, "Bark", "aaa", 111)
    SafeCallMethodWithArgs(pet, "Meow", "aaa", 111)

    // 通过反射，实现插件方式的引入模块
    // 对于有些模块，可能存在有些方法没有实现，可能这个模块不需要实现这个方法
    // 可以通过这样的调用后给出一个清晰的业务提示
}
