#include <unistd.h>  
#include <stdio.h>  
#include <signal.h>  
 
/*

信号的产生有3种方式: 
(1)通过终端快捷键产生信号(比如Ctrl+c,Ctrl+/等); 
(2)调用系统函数向进程发送信号(kill() ,raise(),abort()); 
(3)由软件条件产生信号(alarm(),SIGALRM)

*/

 
void ouch(int sig)  
{  
    printf("\nOUCH! - I got signal %d\n", sig);  
}  
  
int main()  
{  
    struct sigaction act;  
    act.sa_handler = ouch;  
    
    sigemptyset(&act.sa_mask);    //创建空的信号屏蔽字，即不屏蔽任何信息        
    act.sa_flags = SA_RESETHAND;  
    
    /*
    SA_RESETHAND 当调用信号处理函数时，将信号处理器设置为缺省值SIG_DFL, 这句话的意思也就是说当signo信号出现第二次的时候信号处理终止进程，因为第一次接受的时候是将其设置为SIG_DFL
    SA_NODEFER   不在阻塞与处理多个signo相同的信号。
    SA_RESTART   如果信号中断了某个系统调用，则系统会自动启动该系统调用
    SA_SIGINFO   设置了使用新的处理函数， 未设置则使用旧有的处理函数 。
    */
    
    /*
    
    int sigaction(int signo, struct sigaction *act, struct sigaction *oldact) ;

    signo ：需要处理的特定的信号
    act ：设定对信息处理的动作
    oldact ：返回signo信号的当前设置
   
    */
      
    sigaction(SIGINT, &act, 0);  
  
    while(1)  
    {  
        printf("Hello World!\n");  
        sleep(1);  
    }  
    return 0;  
} 
