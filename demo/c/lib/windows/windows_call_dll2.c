/*
隐式链接：
调用的 DLL的主工程的 
*/

#include <stdio.h>
#include <Windows.h>
#include <tchar.h>
 
// 先把 lib 链接进来
#pragma comment (lib , "..//Debug//FuncDll.lib" )

// 外部声明的 add 函数
extern "C" _declspec (dllimport )
      int add(int a, char b); 
int main()
{
    // 直接调用 add 函数
    printf("%d/n" , add(5, 2));
    return 0;
}
