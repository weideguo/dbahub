package main

import (
    "flag"
    "fmt"
    "os"
)

// 在编译时通过 -ldflags 覆盖
var (
    Version   = "dev"
    GitCommit = "unknown"
    BuildTime = "unknown"
)

func main() {
    a := flag.String("a", "A", "aaa")

    flag.Usage = func() {
        // 获取程序名称
        appName := os.Args[0]

        // 打印版本信息
        fmt.Fprintf(os.Stderr, "Usage of %s version %s (commit: %s, built: %s):\n", appName, Version, GitCommit, BuildTime)

        // 默认帮助信息
        flag.PrintDefaults()
    }
    flag.Parse()

    fmt.Println(*a)
}
