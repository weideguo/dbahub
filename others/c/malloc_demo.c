#include <stdio.h>
#include <string.h>
#include <stdlib.h>
 
int main()
{
    char *str;
    
    /* 最初的内存分配 */
    str = (char *) malloc(1);
    strcpy(str, "wadrglkwcvqwweqertqva");
    printf("String = %s,  Address = %u\n", str, str);
    
    /* 重新分配内存 */
    //str = (char *) realloc(str, 2);
    strcat(str, ".xxxq");
    printf("String = %s,  Address = %u\n", str, str);
    
    free(str);
 
 
    char *str1 = NULL;
    str1 = (char *) calloc(1,sizeof(char));
    strcpy(str1, "Hello");
    printf("String = %s,  Address = %u\n", str1, str1);
    free(str1);

 
    return(0);
}


