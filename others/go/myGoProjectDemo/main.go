package main

import (
    "github.com/gin-gonic/gin"

    "github.com/weideguo/myGoProjectDemo/myutils"
)

func main() {
    myutils.PrintStr()
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })
    r.Run("0.0.0.0:9222") // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
