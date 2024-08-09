#include <pthread.h>  
#include <stdio.h>  
#include <stdlib.h>  
#include <unistd.h> 
#include <time.h> 

int x;


// 定义一个互斥锁  
pthread_mutex_t rand_mutex = PTHREAD_MUTEX_INITIALIZER;  

// 参数只能有一个，可以传入结构体实现传入多个参数
void* thread_function(void* arg) {      
    //int r = (rand() % 10)+1;  
    int r = 1;
    
    pthread_t thread_id = pthread_self();  
    
    printf("thread ID: %lu, sleep %d,argument: %s, %d\n", (unsigned long)thread_id, r, (char*)arg, x);  
    sleep(r);  
    
    
    pthread_mutex_lock(&rand_mutex);    // 加锁
    
    x = x+1;
    pthread_mutex_unlock(&rand_mutex);  // 解锁
    
    printf("thread ID: %lu, sleep %d,argument: %s done, %d\n", (unsigned long)thread_id, r, (char*)arg, x);  
    
    
    
    return NULL;  
}

int main() {  
    pthread_t thread_ids[5];  
    char* message = "this is argument";  
    int i;
    
    srand(time(NULL));    // 设置随机种子
    
    // 创建线程  
    for(i=0;i<5;i++){
        if(pthread_create(&thread_ids[i], NULL, thread_function, (void*)message) != 0) {  
            perror("Failed to create thread");  
            return 1;  
        }
    }  
  
    // 等待线程结束  
    for(i=0;i<5;i++){
        if(pthread_join(thread_ids[i], NULL) != 0) {  
            perror("Failed to join thread");  
            return 2;  
        }
    }    
  
    printf("%d\n",x);
    printf("finished\n");  
  
    return 0;  
}
/*
gcc -lpthread
*/
