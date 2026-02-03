package main

import (
    "embed"
    "fmt"
)

//go:embed static/*
var tmplFS embed.FS

func main() {
    content, err := tmplFS.ReadFile("static/hello.txt")
    if err != nil {
        fmt.Println(err.Error())
    }
    fmt.Println(tmplFS)
    fmt.Println(string(content))
}

/*
通过此方式可以将静态文件嵌入golang程序，从而实现打包时只生产一个文件，无需额外静态文件
如编写web前后端分离的代码，通过此方式即可实现嵌入前端代码，再简单设置路由，即可实现编译时打包前端代码
//go:embed xxxxx 是特定语法，必须严格按照此方式设置
*/
