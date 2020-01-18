/*
windows 显示链接
调用的 DLL的主工程的 
*/

#include <stdio.h>
#include <Windows.h>
#include <tchar.h>
 
int main()
{
    HMODULE hModule = NULL;
    typedef int (*Func)(int a, int b); 
    // 动态加载 DLL 文件
    hModule = LoadLibrary(_TEXT("..//Debug//FuncDll.dll" ));
    // 获取 add 函数地址
    Func fAdd = (Func)GetProcAddress(hModule, "add" );
    // 使用函数指针
    printf("%d/n" , fAdd(5, 2));
    // 最后记得要释放指针
    FreeLibrary(hModule);
    return 0;
}