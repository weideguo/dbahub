import stun
import socket
import threading

def handle_stun_request(client_socket, client_address):
    try:
        data, addr = client_socket.recvfrom(1024)
        response = stun.create_response(data)
        client_socket.sendto(response, addr)
    except Exception as e:
        print(f"Error handling STUN request from {client_address}: {e}")
    finally:
        client_socket.close()

def main(server_ip,server_port):
    # 创建 UDP 套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    print(f"STUN server listening on {server_ip}:{server_port}")

    try:
        while True:
            data, addr = server_socket.recvfrom(1024)
            # 为每个请求创建一个新线程 (简单实现)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client_socket.bind((server_ip, 0)) # 使用任意端口
            client_socket.sendto(data, addr) # 回显数据以触发响应
            # 注意：pystun3 的 create_response 需要原始请求数据
            # 这个实现非常简化，实际中需要更复杂的逻辑来解析 STUN 请求
            # pystun3 更多是作为客户端库
            threading.Thread(target=handle_stun_request, args=(client_socket, addr)).start()
    except KeyboardInterrupt:
        print("Shutting down STUN server.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main('0.0.0.0', 3478)