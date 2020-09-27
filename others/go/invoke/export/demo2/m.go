package main
 
/*
 
#include <stdio.h>
//由go实现并导出
int callOnMeGo(int);
 
int callOnMeGo_cgo(int in)
{
    printf("C.callOnMeGo_cgo(): called with arg = %d\n", in);
    //调用GO函数
    return callOnMeGo(in);
}
*/
import "C"
