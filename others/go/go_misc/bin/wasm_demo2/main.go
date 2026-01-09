//go:build js && wasm
// +build js,wasm

package main

import (
    "syscall/js"
)

func add(this js.Value, args []js.Value) any {
    a := args[0].Int()
    b := args[1].Int()
    return a + b
}

func main() {
    // 将 add 函数暴露给 JavaScript 全局作用域（即 window.add）
    js.Global().Set("add", js.FuncOf(add))

    // 阻塞主 goroutine
    select {}
}
