package main

import "fmt"

func mapTest() {
    // var mapname map[keytype]valuetype
    var mapTest map[string]string
    mapTest=map[string]string{"aaa":"AAA","bbb":"BBB"}
    mapTest["aaa"]="ddd"
    mapTest["bbb"]="ccc"
    fmt.Println(mapTest["aaa"])
}

func mapTest2() {
    // var mapname map[keytype]valuetype
    mapTest := make(map[string]string)
    mapTest["aaa"]="aaa111"
    mapTest["bbb"]="bbb111"
    fmt.Println(mapTest)
    // 遍历
    for k, v := range mapTest {
        fmt.Println(k, v)
    }
    // 删除元素
    delete(mapTest, "bbb")
    fmt.Println(mapTest)
    // map没有删除所有元素操作 可以赋值为空 go自带gc

}


func main() {
    //mapTest()
    mapTest2()
}
