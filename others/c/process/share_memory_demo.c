#include<stdio.h>
#include<stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include<string.h>
#include<errno.h>

/*
* 通过共享内存实现进程间通信
*/


typedef struct _T
{
    char name[64];
    int age;
}T;

int main(int argc, char *argv[])
{
    int ret = 0;
    int shmid;

    pid_t pid = fork();

    if(pid == 0)
    {
        shmid = shmget(0x2234, sizeof(T), IPC_CREAT | 0666); //创建共享内存 ，相当于打开文件，文件不存在则创建
        if (shmid == -1)
        {
            perror("shmget err");
            return errno;
        }

        T *p = NULL;

        p = shmat(shmid, NULL, 0);//第二个参数shmaddr为NULL，核心自动选择一个地址 //将共享内存段连接到进程地址空间
        if (p == (void *)-1 )
        {
            perror("shmget err");
            return errno;
        }

        strcpy(p->name, "aaaa");
        //p->name="aaaa";
        p->age = 33;
        printf("input: %s %d\n",p->name,p->age);

        shmdt(p); //将共享内存段与当前进程脱离
    }
    else if(pid > 0)
    {
        shmid = shmget(0x2234, sizeof(T), IPC_CREAT | 0666);
        T *p2 = NULL;
        p2 = shmat(shmid, NULL, 0);
        sleep(3);
        printf("output: %s %d\n",p2->name,p2->age);

        ret = shmctl(shmid, IPC_RMID, NULL);//IPC_RMID为删除内存段
        if (ret < 0)
        {
            perror("rmerrr\n");
        }
    }
    return 0;
}
