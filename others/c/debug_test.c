#include <stdio.h>

int main()
{
    char *px="hello\n";
    while(1)
    {
        
        printf(px);

        sleep(1);
    }

    return 0;
}
/*
gdb -p $pid
*/