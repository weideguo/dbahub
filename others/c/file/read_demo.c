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

    int buffer_size = 100;
    char *buffer = malloc(buffer_size);
    if (buffer == NULL) {
        return 1;
    }
    memset(buffer, '\0', buffer_size);

    //char buffer[100];
    read(fd, buffer, buffer_size);

    close(fd);
    printf(buffer);
    
    umask(mode);
    return 0;
}

