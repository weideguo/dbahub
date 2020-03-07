
#include <stdio.h>
 
#include "clibrary.h"
 
//参数是函数指针

void some_c_func(callback_fcn callback)
{
    int arg = 2;
    printf("C.some_c_func(): arg = %d\n", arg);
    int response = callback(arg);
    printf("C.some_c_func(): response= %d\n", response);
}
