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

/*
open  是POSIX中定义，对应的文件操作有：close, read, write,ioctl 等。
read  不带缓冲

fopen 是标准c里定义，对应的文件操作有：fclose, fread, fwrite, freopen, fseek, ftell, rewind等。
fread 带缓冲

fopen函数返回文件指针，open函数返回文件描述符(整数). 


函数原型：
int open( const char * pathname, int oflags);
int open( const char * pathname, int oflags, mode_t mode);


oflags用于指定文件的打开/创建模式，这个参数可由以下常量（定义于 fcntl.h）通过逻辑或构成。
   O_RDONLY      只读模式 
   O_WRONLY      只写模式 
   O_RDWR        读写模式
以上三者是互斥的，不可以同时使用

打开/创建文件时，至少得使用上述三个常量中的一个。以下常量是选用的：
   O_APPEND         每次写操作都写入文件的末尾 
   O_CREAT          如果指定文件不存在，则创建这个文件 
   O_EXCL           如果要创建的文件已存在，则返回 -1，并且修改 errno 的值
   O_TRUNC          如果文件存在，并且以只写/读写方式打开，则清空文件全部内容 
   O_NOCTTY         如果路径名指向终端设备，不要把这个设备用作控制终端。
   O_NONBLOCK       如果路径名指向 FIFO/块文件/字符文件，则把文件的打开和后继 I/O设置为非阻塞模式（nonblocking mode）。

以下用于同步输入输出
   O_DSYNC          等待物理 I/O 结束后再 write。在不影响读取新写入的数据的前提下，不等待文件属性更新。 
   O_RSYNC          read 等待所有写入同一区域的写操作完成后再进行
   O_SYNC           等待物理 I/O 结束后再 write，包括更新文件属性的 I/O
   O_DIRECT         绕过缓冲区高速缓存，直接I/O

*/
