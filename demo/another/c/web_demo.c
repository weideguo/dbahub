#include <stdio.h>  
#include <string.h>  
#include <sys/socket.h>  
#include <arpa/inet.h>  
#include <unistd.h>  
#include <netinet/in.h>  
#include <stdlib.h>  
  
#define MAXLINE 1024  
  
int main()  
{  
    int sockfd,n;  
    char recvline[MAXLINE];  
    struct sockaddr_in servaddr;  
    char dns[32];  
    char url[128];  
    char *IP = "your_host_ip";  
    char *buf = "GET /forum.php HTTP/1.1\r\n\  
Host: your_host_ip\r\n\  
Proxy-Connection: keep-alive\r\n\  
Cache-Control: max-age=0\r\n\  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n\  
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36\r\n\  
Accept-Encoding: gzip,deflate,sdch\r\n\  
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6\r\n\  
Cookie: P52Q_2132_saltkey=M99iR1So; P52Q_2132_lastvisit=1402616897; P52Q_2132_nofavfid=1; P52Q_2132_visitedfid=2D41D38; P52Q_2132_ulastactivity=63e8Um91gzrgSl71VxWDURz5puThdraSkMWMi3yotj2QHi7O95z5; P52Q_2132_lastcheckfeed=2%7C1404624305; P52Q_2132_editormode_e=1; P52Q_2132_smile=2D1; P52Q_2132_st_t=0%7C1404692476%7Cf1fb107592d1e4dabffd9e8cc052c9bc; P52Q_2132_forum_lastvisit=D_41_1404310798D_2_1404692476; P52Q_2132_seccode=121.8807c72fe7905a644e; P52Q_2132_st_p=0%7C1404692480%7C80767b97b5c8a3d320ed9e0348d982cf; P52Q_2132_viewid=tid_76; P52Q_2132_sid=GQJqQ6; P52Q_2132_lastact=1404693952%09forum.php%09ajax\r\n\  
\r\n";  //*/
    if((sockfd = socket(AF_INET,SOCK_STREAM,0)) < 0)  
        printf("socket error\n");  
    printf("1\n");  
    bzero(&servaddr,sizeof(servaddr));  
    servaddr.sin_family = AF_INET;  
    servaddr.sin_port = htons(80);  
    if(inet_pton(AF_INET,IP,&servaddr.sin_addr) <= 0)  
        printf("inet_pton error\n");  
    if(connect(sockfd,(struct sockaddr *)&servaddr,sizeof(servaddr)) < 0)  
        printf("connect error\n");  
    write(sockfd,buf,strlen(buf));  
    printf("%s\n\n",buf);  
    while((n = read(sockfd,recvline,MAXLINE)) > 0)  
    {  
        recvline[n] = 0;  
        if(fputs(recvline,stdout) == EOF)  
            printf("fputs error\n");  
    }  
    if(n < 0)  
        printf("read error\n");  
    printf("all ok now\n");  
    exit(0);  
} 
