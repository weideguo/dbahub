/*
JNA 
(Java Native Access)

*/

#define MYLIBAPI  


extern "C" __declspec( dllexport ) 
    MYLIBAPI void say(wchar_t* pValue);
 
void  say(wchar_t* pValue){ 
    std::wcout<<L"上帝说："<<pValue<<std::endl;
}


/*
编译成dll
g++ -Wall -D_JNI_IMPLEMENTATION_ -Wl,--kill-at -Id:/java/include –Id:/java/include/win32 -shared -o TestDll.dll my_jna_test.c

*/