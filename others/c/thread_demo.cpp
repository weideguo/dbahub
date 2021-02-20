#include <iostream>
#include <unistd.h>
#include <pthread.h>
 
using namespace std;
 
#define NUM_THREADS 5
 

void* say_hello(void* args)
{
    sleep(1);
    cout << "Hello Thread！" << endl;
    return 0;
}
 
int main()
{
    
    pthread_t tids[NUM_THREADS];
    for(int i = 0; i < NUM_THREADS; ++i)
    {
        //参数依次是：线程id，线程参数，调用的函数，传入的函数参数（需要为指针类型，可以通过传入指向结构体的指针实现多个参数传递）
        int ret = pthread_create(&tids[i], NULL, say_hello, NULL);
        if (ret != 0)
        {
           cout << "pthread_create error: error_code=" << ret << endl;
        }
    }
    
    pthread_exit(NULL);
}

/*
#使用的线程方法需要调用操作系统提供的动态链接库
g++ thread_demo.cpp -lpthread -o thread_demo 
*/

/*
pthread_join (threadid, status) 
pthread_detach (threadid) 
*/