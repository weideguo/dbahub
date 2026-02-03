package main

import "go_misc/cmd/plugin_demo2/plugin"

func main() {
    // 由此可以实现通过运行参数选择插件
    selectedFrontend := "m2"
    be, ok := plugin.AllBackends[selectedFrontend]
    if !ok {
        panic(ok)
    }
    be.Setup()
    be.Fetch("hello")
}
