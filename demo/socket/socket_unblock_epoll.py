#coding:utf8
from socket import *
import select



socket_server = socket(AF_INET, SOCK_STREAM)
socket_server.bind(("", 7789))
socket_server.listen(5)

epoll = select.epoll()
# 注册主套接字,监控读状态
epoll.register(socket_server.fileno(), select.EPOLLIN)

sock_dicts = {}
client_dicts = {}
while True:
    """
    没有文件描述符最大数量的限制(最大数量则看内存大小)；
    采用时间通知机制，当文件描述符状态有变时，主动通知内核进行调度
    """
    # 程序阻塞在这，返回文件描述符有变化的对象
    poll_list = epoll.poll()
    print(poll_list)
    for socket_fileno, events in poll_list:
        
        if socket_fileno == socket_server.fileno():
            # 创建新套接字
            new_sock, client_info = socket_server.accept()
            print("client: %s" % str(client_info))
            # 注册到epoll监测中
            epoll.register(new_sock.fileno(), select.EPOLLIN)
            
            sock_dicts[new_sock.fileno()] = new_sock
            client_dicts[new_sock.fileno()] = client_info
        else:
            # 接收消息
            raw_data = sock_dicts[socket_fileno].recv(1024)
            if raw_data:
                print("recv %s %s " % (str(client_dicts[socket_fileno]), raw_data))
            else:
                # 关闭连接
                sock_dicts[socket_fileno].close()
                # 注销epoll监测对象
                epoll.unregister(socket_fileno)
                
                del sock_dicts[socket_fileno]
                del client_dicts[socket_fileno]
         
        print(sock_dicts)
        print(client_dicts)



"""
EPOLLIN （可读）
EPOLLOUT （可写）
EPOLLET （ET模式）
LT模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序可以不立即处理该事件。下次调用epoll时，会再次响应应用程序并通知此事件。

ET模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序必须立即处理该事件。如果不处理，下次调用epoll时，不会再次响应应用程序并通知此事件。

"""
