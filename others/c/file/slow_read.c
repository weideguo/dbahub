#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>


const char *filename = "/tmp/test.txt";
int main()
{
    mode_t mode;
    mode=umask(0000);
    int fd=open( filename ,O_RDWR, 0666);
    if(fd== -1){
        printf( "open file failed");
        umask(mode);
        exit( -1);
    }

    int buffer_size = 5;
    char *buffer = malloc(buffer_size);
    if (buffer == NULL) {
        return 1;
    }
    
    char str1[5];
    
    while(1) {
        printf("\nany input %d chars to continue: ", sizeof(str1));
        scanf("%s", str1); 
        memset(buffer, '\0', buffer_size);
        read(fd, buffer, buffer_size);
        printf(buffer);
    }

    close(fd);
    umask(mode);
    return 0;
}

/*
用于验证一个进程打开文件后，其他进程更改文件的情况

实测当前进程打开文件后
删除（rm）、移动文件（mv）、移动后新建同名文件（mv/touch），依旧可以读取原始的文件内容；
直接编辑原始文件，保存后则读取到新的内容；

*/
