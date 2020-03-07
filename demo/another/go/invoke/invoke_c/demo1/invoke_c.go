package main

/*
#include <stdio.h>
#include <stdlib.h>
typedef struct {
    int id;
}ctx;
ctx *createCtx(int id) {
    ctx *obj = (ctx *)malloc(sizeof(ctx));
    obj->id = id;
    return obj;
}
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
直接在源代码通过注释引入c语言，通过import "C"引用，c的源码与引用之间不能存在其他字符，空行也不行
编译后不再依赖其他源码文件
*/
