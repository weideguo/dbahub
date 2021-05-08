#include <stdio.h>
#include <dlfcn.h>     


int main(){  
    void* handler = dlopen("./libfunc.so",RTLD_LAZY);    //运行时需要依赖链接库 gcc func.c -shared -fPIC -o libfunc.so
    //int (*fun)(int,int) = dlsym(handler,"add");  
    //int result = fun(34,25);  
    //printf("result %d\n",result);
    
    void (*fun)() = dlsym(handler,"func");  
    fun();  
}
/*
libdl.so  编译时需要依赖链接库
gcc -L/usr/lib64 -ldl  call_func2.c
*/