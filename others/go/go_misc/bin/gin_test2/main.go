package main

import (
    "net/http"

    "github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default()

    // 文件上传接口
    r.POST("/upload", func(c *gin.Context) {
        // 获取文件
        file, err := c.FormFile("file")
        if err != nil {
            c.JSON(http.StatusBadRequest, gin.H{
                "message": "File is required",
            })
            return
        }

        // 保存文件到本地
        err = c.SaveUploadedFile(file, "./"+file.Filename)
        if err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{
                "message": "Failed to save file",
            })
            return
        }

        // 返回成功响应
        c.JSON(http.StatusOK, gin.H{
            "message": "File uploaded successfully",
            "file":    file.Filename,
        })
    })

    // 启动 Gin 服务
    r.Run(":8081")
}
