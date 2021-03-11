#include <stdio.h>
#include <curl/curl.h>

#define URL "http://127.0.0.1:8222/"

size_t write_data(void *buffer, size_t size, size_t nmemb, void *userp)
{
  return size * nmemb;
}

void sendMessage(char *message) {
    //char url[500];
    char data[200];
    
    snprintf(data,300,"text=%s",message);
    //printf(data);
    CURL *curl;
    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, URL);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data); 
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
        curl_easy_perform(curl);      //发送并等待回应
        printf("sending....\n");
    }    
    curl_global_cleanup();
    printf("send done\n");
}

int main(int argc,char *argv[]){
    char *message;
    message = argv[1];
    
    sendMessage(message);
    
    return 0;
}

/*
yum install curl-devel
gcc -lcurl curl_demo.c -o curl_demo
*/
