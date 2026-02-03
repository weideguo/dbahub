package main

import (
    "net/http"

    "github.com/gin-gonic/gin"
)

func main() {
    app := gin.New()

    // 设置默认路由
    defaultGroup := app.Group("/")
    {
        // 设置默认处理函数
        defaultGroup.GET("", func(c *gin.Context) {
            c.String(http.StatusOK, "Welcome to the default path!")
        })
    }

    //apiGroup := app.Group("/api")
    //{
    //  完整路径则为 /api/a
    //  apiGroup.GET("a", )
    //}

    app.NoRoute(func(c *gin.Context) {
        c.JSON(http.StatusNotFound, gin.H{
            "message": "not found",
        })
    })

    app.Run("0.0.0.0:8080")
}
