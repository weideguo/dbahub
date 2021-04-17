#include <stdlib.h>
#include <fcntl.h>


const char *filename = "/tmp/test.txt";
const char str[] = "hello\n";
int main()
{
    mode_t mode;
    mode=umask( 000 );
    int fd=open( filename ,O_RDWR|O_CREAT|O_EXCL, 00666);        // chmod 666 /tmp/test.txt
    if(fd== -1){
        umask(mode);
        exit( -1);
    }
    
    write(fd, str , sizeof(str));
    close(fd);
    umask(mode);
    return 0;
}

/*
O_RDONLY 只读方式 O_WRONLY 只写，O_RDWR读写，O_CREAT创建，O_EXCL文件如果存在返回错误

open和fopen的区别：
前者属于低级IO，后者是高级IO。
前者返回一个文件描述符，后者返回一个文件指针。
前者无缓冲，后者有缓冲。
前者与 read, write 等配合使用， 后者与 fread, fwrite等配合使用。
后者是在前者的基础上扩充而来的，在大多数情况下，用后者。 

#include <unistd.h>

off_t lseek(int fd, off_t offset, int whence);
 
offset：表示从文件的whence位置开始偏移的位置大小。
whence：表示文件偏移的位置
  SEEK_SET：表示从文件开始位置偏移
  SEEK_CUR：表示从文件当前的读写位置偏移
  SEEK_END：表示从文件的结束位置偏移
*/

