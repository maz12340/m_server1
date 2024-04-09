import socket


HOST = '127.0.0.1'
PORT = 12345


def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    return client


def send_message(socket):
    message = input('Введите сообщение для отправки: ')
    socket.send(message.encode())
    response = socket.recv(1024)
    print('Получено:', response.decode())


if __name__ == "__main__":
    client = connect_to_server()

    while True:
        send_message(client)
 
