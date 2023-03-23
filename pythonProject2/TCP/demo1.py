import socket

if __name__ == '__main__':

    tcp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket_client.connect(('192.168.10.8', 9090))
    send_content = input('输入要发送的数据：')
    send_data = send_content.encode('utf-8')
    tcp_socket_client.send(send_data)
    recv_data = tcp_socket_client.recv(1024)
    print(recv_data)
    tcp_socket_client.close()
