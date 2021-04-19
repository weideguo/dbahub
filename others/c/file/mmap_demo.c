/*
内存映射文件

mmap系统调用使得进程之间通过映射同一个普通文件实现共享内存。
普通文件被映射到进程地址空间后，进程可以像访问普通内存一样对文件进行访问，不必再调用read()，write（）等操作。

*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>

const char *filename = "/tmp/test.txt";

typedef struct{
    char name[20];
    //char *name;
    short age;
    float score;
    char sex;
}student;

int write_file() {
    student stu[5];
    mode_t mode;
    mode=umask( 000);
    int fd=open(filename,O_RDWR|O_CREAT|O_EXCL, 00666);
    if(fd== -1){
        printf( "open:%m\n");
        umask(mode);
        exit( -1);
    }
    memset(stu, 0, sizeof(stu));
    int i= 0;
    for(;i< 5;i++){
        //stu[i].name="tomx";  //不能由此赋值  char *name; 这种声明才能用此
        
        char *name="tom";
        memcpy(stu[i].name, name, strlen(name)+ 1);
        
        stu[i].age   = i;
        stu[i].score = 89.12f;
        stu[i].sex   = 'm';
        write(fd,&stu[i], sizeof(stu[i]));
    }
    close(fd);
    umask(mode);
    return 0;   
}

int main()
{
    //write_file();
    
    student *p,*pend;  
    //打开文件描述符号
    int fd;
    /*打开文件*/
    fd=open(filename,O_RDWR);
    if(fd==-1){//文件不存在
        printf("打开文件失败:%m\n");
        exit(-1);
    }
    
    //获取文件的大小，映射一块和文件大小一样的内存空间，如果文件比较大，可以分多次，一边处理一边映射；
    struct stat st; //定义文件信息结构体
    /*取得文件大小*/
    int r=fstat(fd,&st);
    if(r==-1){
        printf("获取文件大小失败:%m\n");
        close(fd);
        exit(-1);
    }
    int len=st.st_size;    
    /*把文件映射成虚拟内存地址*/
    p=mmap(NULL,len,PROT_READ|PROT_WRITE,MAP_SHARED,fd,0);    
    if(p==NULL || p==(void*)-1){
        printf("映射失败:%m\n");
        close(fd);
        exit(-1);
    }
    /*通过内存读取记录*/
    
    int i=0;
    while(i<(len/sizeof(student)))
    {
        printf("----------------%d--------------------------\n",i);
        printf("name=%s\n", p[i].name);
        printf("age=%d\n",  p[i].age);
        printf("score=%f\n",p[i].score);
        printf("sex=%c\n",  p[i].sex);
        i++;
    }  

    // 修改数据
    p[1].sex = 'f';
    
        
    // // 同步到磁盘文件
    // if((msync((void *)p, st.st_size, MS_SYNC)) == -1){
    //     printf("msync error\n");
    //     exit(-1);
    // }
    
    // 只同步部分到磁盘
    if((msync((void *)(p+sizeof(student)), sizeof(student), MS_SYNC)) == -1){
        printf("msync error\n");
        exit(-1);
    }
    
    /*释放映射区*/
    munmap(p,len);
    /*关闭文件*/    
    close(fd);    
}

