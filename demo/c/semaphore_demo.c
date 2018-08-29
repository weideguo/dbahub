#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/sem.h>

/*
* 使用信号量控制进程并发
* 测试：
* gcc semaphore_demo.c -o semaphore_demo
* ./semaphore_demo 1 1 & semaphore_demo
*/


union semun
{
    int val;
    struct semid_ds *buf;
    unsigned short *arry;
};
 
static int sem_id = 0;
 
static int init_semvalue();  // 初始化信号量
static void del_semvalue();  // 删除信号量
static int semaphore_p();    // 进入临界区
static int semaphore_v();    // 离开临界区 
 
int main(int argc, char *argv[])
{
    char message = 'X';
    int i = 0;
    sem_id = semget((key_t)1234, 1, 0666 | IPC_CREAT); /* 创建信号量 */
 
    if(argc > 1)
    {       
        if(!init_semvalue()) 
        {
            fprintf(stderr, "Failed to initialize semaphore\n");
            exit(EXIT_FAILURE);
        }       
        message = argv[1][0];
        sleep(2);
    }

    for(i = 0; i < 10; ++i)
    {       
        if(!semaphore_p())          /* 进入临界区 */
        {
            exit(EXIT_FAILURE);
        }
        
        
        printf("%d  %c\n", getpid(),message);  //对于相同信号量，一次只能允许一个进程进入临界区 
                                               //这部分将可以原子化操作
        sleep(rand() % 3);                     //
                                               //
        printf("%d  %c\n", getpid(),message);  //
        
        
        if(!semaphore_v())          /* 离开临界区 */
        {
            exit(EXIT_FAILURE);
        }
    }

    printf("\n%d - finished\n", getpid()); 
    if(argc > 1)
    {        
        del_semvalue();  
    }
    exit(EXIT_SUCCESS);
}
 
static int init_semvalue()
{   
    union semun sem_union;
    sem_union.val = 1;
    if(semctl(sem_id, 0, SETVAL, sem_union) == -1)
    {
        return 0;
    }
    return 1;
}
 
static void del_semvalue()
{   
    union semun sem_union;
    if(semctl(sem_id, 0, IPC_RMID, sem_union) == -1)
    {
         fprintf(stderr, "Failed to delete semaphore\n");
    }
}

static int semaphore_p()
{
    /* 对信号量做减1操作，即等待P（sv）*/
    struct sembuf sem_b;
    sem_b.sem_num = 0;
    sem_b.sem_op = -1; //P()
    sem_b.sem_flg = SEM_UNDO;
    if(semop(sem_id, &sem_b, 1) == -1)
    {
        fprintf(stderr, "semaphore_p failed\n");
        return 0;
    }
    return 1;
}
 
static int semaphore_v()
{
    /* 对信号量做加1操作，即发送信号V（sv）*/
    struct sembuf sem_b;
    sem_b.sem_num = 0;
    sem_b.sem_op = 1; //V()
    sem_b.sem_flg = SEM_UNDO;
    if(semop(sem_id, &sem_b, 1) == -1)
    {
        fprintf(stderr, "semaphore_v failed\n");
        return 0;
    }
    return 1;
}
