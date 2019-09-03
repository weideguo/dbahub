
#include<stdio.h>

void func()
{
    printf("func world/n");
}
/*
编译成so	
gcc func.c -shared -fPIC -o libfunc.so
*/