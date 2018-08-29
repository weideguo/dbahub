#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>


int main()
{
    int fd[2];
    int ret = pipe(fd);  // fd为两个文件描述符,fd[0]指向管道的读端,fd[1]指向管道的写端。fd[1]的输出是fd[0]的输入。
    if (ret == -1)
    {
        perror("pipe error\n");
        return 1;
    }
    pid_t id = fork();
    if (id == 0)  //child
    {
        close(fd[0]);
        char *child = "I am  child!";
        int i = 0;
        while (i<5)
        {
            write(fd[1], child, strlen(child) + 1);
            sleep(2);
            i++;
        }
    }
    else if (id>0)  //father
    {
        close(fd[1]);
        char msg[100];
        int j = 0;
        while (j<5)
        {
            memset(msg,"\0",sizeof(msg));
            ssize_t s = read(fd[0], msg, sizeof(msg));
            if (s>0)
            {
                msg[s - 1] = "\0";
            }
            //printf("output:");
            printf("%s\n", msg);
            j++;
        }
    }

    return  0;
}
