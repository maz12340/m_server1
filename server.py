import socket
import threading


HOST = '127.0.0.1'
PORT = 12345


def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        client_socket.send(request)


def echo_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    while True:
        client, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == "__main__":
    echo_server()
