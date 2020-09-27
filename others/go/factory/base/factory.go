package base

type Class interface {
    Do()
}
var (
    factoryByName = make(map[string]func() Class)
)
// 注册
func Register(name string, factory func() Class) {
    factoryByName[name] = factory
}
// 根据名称 调用对应的方法实例化结构体
func Create(name string) Class {
    if f, ok := factoryByName[name]; ok {
        return f()
    } else {
        panic("name not found")
    }
}
