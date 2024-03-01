#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{
    printf("%f\n",exp(1));
    return 0;
}
/*
gcc math_demo.c -lm
gcc math_demo.c -L/usr/lib64/libm.so
*/
