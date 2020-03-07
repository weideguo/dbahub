package main

/*
#include "test.c"
*/
import "C"

import (
	"fmt"
)

func main() {
	var ctx *C.ctx = C.createCtx(100)
	fmt.Printf("id : %d\n", ctx.id)
}
/*
c代码通过注释的include语句引入
*/
