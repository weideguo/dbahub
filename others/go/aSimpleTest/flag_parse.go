package main

import (
	"flag"
	"fmt"
)

// 定义命令行参数
var mode = flag.String("mode", "default_value", "help时提示的注释")

func main() {

	flag.Parse()
    
	fmt.Println(*mode)
}
/*
./flag_parse --help

./flag_parse --mode xxx

*/