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
