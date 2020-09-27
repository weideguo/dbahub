package main
import "fmt"
// 定义飞行动物接口
type Flyer interface {
    Fly()
}
// 定义行走动物接口
type Walker interface {
    Walk()
}
// 定义鸟类
type bird struct {
}
// 实现飞行动物接口
func (b *bird) Fly() {
    fmt.Println("bird: fly")
}
// 为鸟添加Walk()方法, 实现行走动物接口
func (b *bird) Walk() {
    fmt.Println("bird: walk")
}
// 定义猪
type pig struct {
}
// 为猪添加Walk()方法, 实现行走动物接口
func (p *pig) Walk() {
    fmt.Println("pig: walk")
}
func f1() {
    // 创建动物的名字到实例的映射
    animals := map[string]interface{}{
        "bird": new(bird),
        "pig":  new(pig),
    }
    // 遍历映射
    for name, obj := range animals {
        
        // t,ok := i.(T) // T 可以为类型、接口
        // 判断对象是否为飞行动物
        f, isFlyer := obj.(Flyer)
        // 判断对象是否为行走动物
        w, isWalker := obj.(Walker)
        fmt.Printf("name: %s isFlyer: %v isWalker: %v\n", name, isFlyer, isWalker)
        // 如果是飞行动物则调用飞行动物接口
        if isFlyer {
            f.Fly()
        }
        // 如果是行走动物则调用行走动物接口
        if isWalker {
            w.Walk()
        }
    }
}


func f2(){
    p1 := new(bird)
    var a Walker = p1
    //p2,ok2 := a.(*pig)
    p2,ok2 := a.(*bird)   //t := i.(T)  // i 没有完全实现 T 接口的方法, 这个语句将会运行错误 因而最好都加上两个参数
    fmt.Printf("p1=%p p2=%p ok2=%b \n", p1, p2 ,ok2)
    p1.Fly()
    p2.Fly()   //a的属性被修减 但p2的没有
    
    //x := "xxx"
    //fmt.Println(*&x)
}


func main(){
    // f1()
    f2()
}


