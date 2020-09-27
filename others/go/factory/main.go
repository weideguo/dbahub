package main
import (
    "./base"
    _ "./p1"  // 匿名引用包, 自动注册
)
func main() {
    // 使用工厂创建Class1实例
    c1 := base.Create("Class1")
    c1.Do()
}
