#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 8888
#define MAX_CLIENTS 30
#define BUFFER_SIZE 1024

int main() {
    int listen_fd, client_fd, max_fd, activity, i, ret;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_len = sizeof(client_addr);
    char buffer[BUFFER_SIZE];

    // 1. 创建监听 socket
    listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (listen_fd < 0) {
        perror("socket");
        exit(EXIT_FAILURE);
    }

    // 设置端口复用，避免 "Address already in use"
    int opt = 1;
    setsockopt(listen_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    if (bind(listen_fd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("bind");
        close(listen_fd);
        exit(EXIT_FAILURE);
    }

    if (listen(listen_fd, 10) < 0) {
        perror("listen");
        close(listen_fd);
        exit(EXIT_FAILURE);
    }

    printf("Echo server running on port %d\n", PORT);

    // 准备 fd_set
    fd_set read_fds, master_fds;
    FD_ZERO(&read_fds);
    FD_ZERO(&master_fds);
    FD_SET(listen_fd, &master_fds);
    max_fd = listen_fd;

    // 存储所有客户端 socket
    int client_sockets[MAX_CLIENTS];
    for (i = 0; i < MAX_CLIENTS; i++) { 
        client_sockets[i] = 0;
    }

    // 事件循环
    while (1) {
        read_fds = master_fds;  // 每次 select 前复制
        activity = select(max_fd + 1, &read_fds, NULL, NULL, NULL);
        printf("New loop\n");  
        /*
        通过select，实现事件等待，在这里为网络输入触发动作
        如果没有事件等待而直接用循环，会导致可能出现循环空转CPU升高
        
        // 读取标准输入的事件
        fd_set read_fds;
        FD_ZERO(&read_fds);
        FD_SET(STDIN_FILENO, &read_fds);
        struct timeval timeout = {5, 0};
        int ret = select(STDIN_FILENO + 1, &read_fds, NULL, NULL, &timeout);
        
        */

        if (activity < 0 && errno != EINTR) {
            perror("select");
            break;
        }

        // 检查监听 socket 是否有新连接
        if (FD_ISSET(listen_fd, &read_fds)) {
            client_fd = accept(listen_fd, (struct sockaddr*)&client_addr, &addr_len);
            if (client_fd < 0) {
                perror("accept");
                continue;
            }

            printf("New connection from %s:%d, fd=%d\n",
                   inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port), client_fd);

            // 将新 client fd 加入 master 集合
            FD_SET(client_fd, &master_fds);
            if (client_fd > max_fd) max_fd = client_fd;

            // 存入 client_sockets 数组
            for (i = 0; i < MAX_CLIENTS; i++) {
                if (client_sockets[i] == 0) {
                    client_sockets[i] = client_fd;
                    break;
                }
            }
        }

        // 检查所有已有 client socket 是否有数据可读
        for (i = 0; i < MAX_CLIENTS; i++) {
            int sock = client_sockets[i];
            if (sock == 0) continue;

            if (FD_ISSET(sock, &read_fds)) {
                memset(buffer, 0, BUFFER_SIZE);
                ret = read(sock, buffer, BUFFER_SIZE - 1);

                if (ret <= 0) {
                    // 连接关闭或出错
                    if (ret == 0) {
                        printf("Client fd=%d disconnected\n", sock);
                    } else {
                        perror("read");
                    }

                    close(sock);
                    FD_CLR(sock, &master_fds);
                    client_sockets[i] = 0;
                    continue;
                }

                // 回显数据给客户端
                printf("Received from fd=%d: %s", sock, buffer);
                send(sock, buffer, ret, 0);
            }
        }
    }

    // 清理
    close(listen_fd);
    for (i = 0; i < MAX_CLIENTS; i++) {
        if (client_sockets[i] != 0) close(client_sockets[i]);
    }
    return 0;
}
/*
事件循环示例
*/
