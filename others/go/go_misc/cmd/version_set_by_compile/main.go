package main

import "fmt"

// 在编译时通过 -ldflags 覆盖
var (
    Version   = "dev"
    GitCommit = "unknown"
    BuildTime = "unknown"
)

func main() {
    fmt.Printf("Version:   %s\n", Version)
    fmt.Printf("GitCommit: %s\n", GitCommit)
    fmt.Printf("BuildTime: %s\n", BuildTime)
}

/*
# 编译
GIT_COMMIT=$(git rev-parse --short HEAD)
# BUILD_TIME=$(date '+%Y-%m-%dT%H:%M:%S%z')  # 使用当地时间
BUILD_TIME=$(date -u '+%Y-%m-%dT%H:%M:%SZ')  # 使用utc+0时间
VERSION=0.0.1
go build -ldflags "-X main.GitCommit=${GIT_COMMIT} -X main.BuildTime=${BUILD_TIME} -X main.Version=${VERSION}"
*/
