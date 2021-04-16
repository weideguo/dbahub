/*
一般情况下，对硬盘（或者其他持久存储设备）文件的write操作，更新的只是内存中的页缓存（page cache），
而脏页面不会立即更新到硬盘中，而是由操作系统统一调度，如由专门的flusher内核线程在满足一定条件时（如一定时间间隔、内存中的脏页达到一定比例）内将脏页面同步到硬盘上（放入设备的IO请求队列）。

因为write调用不会等到硬盘IO完成之后才返回，因此如果OS在write调用之后、硬盘同步之前崩溃，则数据可能丢失。
虽然这样的时间窗口很小，但是对于需要保证事务的持久化（durability）和一致性（consistency）的数据库程序来说，write()所提供的“松散的异步语义”是不够的，通常需要OS提供的同步IO（synchronized-IO）原语来保证。

sync函数只是将所有修改过的块缓冲区排入写队列，然后就返回，它并不等待实际写磁盘操作结束。
fsync功能是确保文件fd所有已修改的内容已经正确同步到硬盘上，该调用会阻塞等待直到设备报告IO完成。数据库类型应用可能需要使用。
fdatasync函数类似于fsync，但它只影响文件的数据部分。而除数据外，fsync还会同步更新文件的属性。
*/
#include <stdio.h>
#include <stdlib.h>


const char *filename = "/tmp/test.txt";
const char str[] = "hello\n";

int write_file(const char *message) {
    FILE *fp = fopen(filename, "a+");
    
    int i;
    //for(i=0;i<10;i++) {
    for(i=0;i<10;) {
        if (fwrite(str, sizeof(str), 1, fp) <= 0) {
            break;
            printf("fwrite error");
        }
        fflush(fp);                //可能有fwrite没写完的部分， flush 内存缓存 到 fp 缓存， 刷新流 stream 的输出缓冲区
        
        fsync(fileno(fp));         //写入磁盘 
        //fdatasync(fileno(fp));
        //sync();
        
        sleep(1); 
    };
    fclose(fp);
}

int main(int argc,char *argv[]){
    char *message;
    message = argv[1];
    write_file(message);
    
    return 0;
}


/*

#include <unistd.h>

off_t lseek(int fd, off_t offset, int whence);
 
offset：表示从文件的whence位置开始偏移的位置大小。
whence：表示文件偏移的位置
  SEEK_SET：表示从文件开始位置偏移
  SEEK_CUR：表示从文件当前的读写位置偏移
  SEEK_END：表示从文件的结束位置偏移



fwrite

ptr     指向要被写入的元素数组的指针。
size    要被写入的每个元素的大小，以字节为单位。
nmemb   元素的个数，每个元素的大小为 size 字节。
stream  指向 FILE 对象的指针，该 FILE 对象指定了一个输出流。
*/

