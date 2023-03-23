import socket

if __name__ == '__main__':
    tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_sever_socket.bind(('', 9090))

    tcp_sever_socket.listen(128)

    new_client, ip_port = tcp_sever_socket.accept()
    print('客户端的Ip和端口号 ：',ip_port)


    recv_data = new_client.recv(1024)

    print(recv_data.decode('utf-8'))

    send1 = input('要发送的数据：')
    send_data = send1.encode('utf-8')
    new_client.send(send_data)
    new_client.close()

    tcp_sever_socket.close()

