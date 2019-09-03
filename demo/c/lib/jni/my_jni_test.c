#include <jni.h>
#include "kg_tom_MyJni.h"
#include <stdio.h>
 
JNIEXPORT void JNICALL Java_kg_tom_MyJni_display(JNIEnv *env, jobject obj)
{
    printf("Hello World tom!!");
    return;
}
 
JNIEXPORT jdouble JNICALL Java_kg_tom_MyJni_sum(JNIEnv *env, jobject obj, jdouble a, jdouble b)
{
    return a + b;
}

/*

mingw方式在windows下安装gcc

编译成dll
gcc -Wall -D_JNI_IMPLEMENTATION_ -Wl,--kill-at -Id:/java/include –Id:/java/include/win32 -shared -o sum.dll my_jni_test.c

-Wall -D_JNI_IMPLEMENTATION_	把C文件编译成dll
-Wl,--kill-at  					因为mingw默认是用@来进行分隔,会导致JNI机制不能读取,所以要删掉？？？
Id:/java/include   				导入jni需要的头文件
-shared -o						输出配置
*/