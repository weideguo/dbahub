#include <stdio.h>
#include <signal.h>
#include <unistd.h>
 
static void sig_usr(int);
int main(void)
{
    if(signal(SIGUSR1, sig_usr) == SIG_ERR)
    { printf("can not catch SIGUSR1\n"); }
    
    if(signal(SIGUSR2, sig_usr) == SIG_ERR)
    { printf("can not catch SIGUSR2\n"); }
       
    if(signal(SIGHUP, sig_usr) == SIG_ERR)
    { printf("can not catch SIGUSR2\n"); }       
        
    for(;;)
    {
        pause();
    }           
}
 
static void sig_usr(int signo)
{
    if(signo == SIGUSR1)
    { printf("received SIGUSR1\n");}  
    else if(signo == SIGUSR2)
    { printf("received SIGUSR2\n");}    
    else
    { printf("received signal %d\n", signo);}       
}
/*
kill -USR1 $pid     # 等同于 kill -10  $pid
kill -USR2 $pid     # 等同于 kill -12  $pid
kill -HUP  $pid     # 等同于 kill -1  $pid

即自行处理这些信号，而不是默认的终止进程

也可以在代码中调用系统函数发出信号
kill(pid, SIGUSR1)
kill(pid, SIGUSR2)
*/

