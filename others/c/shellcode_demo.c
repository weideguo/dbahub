#include <stdio.h>

int main() {
    
    unsigned char shellcode[] = 
        "\x48\xc7\xc0\x01\x00\x00\x00" // mov rax, 1
        "\x48\xc7\xc7\x01\x00\x00\x00" // mov rdi, 1
        "\x48\x8d\x35\x12\x00\x00\x00" // lea rsi, [rip+18]
        "\x48\xc7\xc2\x06\x00\x00\x00" // mov rdx, 6
        "\x0f\x05"                     // syscall
        "\x48\xc7\xc0\x3c\x00\x00\x00" // mov rax, 60
        "\x0f\x05"                     // syscall
        "\x68\x65\x6c\x6c\x6f\x0a";    // "hello\n"

    
    // 强制转换为函数指针并执行
    ((void (*)())shellcode)();
    
    return 0;
}
/*
gcc -z execstack -no-pie -o shellcode_demo shellcode_demo.c
*/
