package main

import (
    "embed"
    "io/fs"
    "net/http"

    "github.com/gin-gonic/gin"
)

//go:embed dist
var staticFS embed.FS

func main() {
    app := gin.New()

    fp, _ := fs.Sub(staticFS, "dist")
    app.StaticFS("/", http.FS(fp))

    app.Run("0.0.0.0:8080")
}

/*
打包web静态文件，编译到dist目录

访问路径 http://127.0.0.1:8080/static/a.html

*/
