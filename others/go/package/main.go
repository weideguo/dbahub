package main

//查找当前目录下目录demo下的包 新版本不要再使用该方式，改用go mod管理 ！！！！！！！
//可以使用 "." ".."改变目录  （go1.13以及之后不可以使用该方式 go1.7可以）
import "./demo"


func main() {
    demo.PrintStr()
}

