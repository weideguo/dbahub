package main

import "fmt"

func f1(){
    // 空接口类型可以保存任何值，也可以从空接口中取出原值。
    var any interface{}
    any = 1 
    any = "xxx"   //因为定义为接口类型 可以重新设置为不同的类型;否则不能覆盖设置
    fmt.Println(any)
}

func f2(){
    var a int = 1
    var i interface{} = a
    // var b int = i      //不能从接口获取值到非接口类型
    var b int = i.(int)
    fmt.Println(b)

    var c int = 10        //同类型的接口才能比较 否则会出错
    fmt.Println(a==c)
    
    var d interface{} = []int{10}
    var e interface{} = []int{10,20}    //两个动态类型值不能对比
    fmt.Println(d,e)

    var f interface{} = []int{10}
    var j interface{} = [1]int{10}      //不都为动态值则可以对比
    fmt.Println(f==j)
}

func f3(v interface{}) {
    switch v.(type) {
    case int:
        fmt.Println(v, "is int")
    case string:
        fmt.Println(v, "is string")
    case bool:
        fmt.Println(v, "is bool")
    }
    // 可以使用自定义的接口判断

}

//不能再函数中存在函数
//////////////////////////////////////////
// 电子支付方式
type Alipay struct {
}
// 为Alipay添加CanUseFaceID()方法, 表示电子支付方式支持刷脸
func (a *Alipay) CanUseFaceID() {
}
// 现金支付方式
type Cash struct {
}
// 为Cash添加Stolen()方法, 表示现金支付方式会出现偷窃情况
func (a *Cash) Stolen() {
}
// 具备刷脸特性的接口
type CantainCanUseFaceID interface {
    CanUseFaceID()
}
// 具备被偷特性的接口
type ContainStolen interface {
    Stolen()
}

func print(payMethod interface{}) {
    switch payMethod.(type) {
    case CantainCanUseFaceID:  // 可以刷脸
        fmt.Printf("%T can use faceid\n", payMethod)
    case ContainStolen:  // 可能被偷
        fmt.Printf("%T may be stolen\n", payMethod)
    }
}

func f4() {
print(new(Alipay))

print(new(Cash))
}
///////////////////////////////////////////////////////

func main(){
    //f1()
    //f2()
    //f3(true)
    f4()
}


