# Name:     Piam Pan Ya Chittisane
# UARK ID:  010868460

import socket


def server_program():
    host = socket.gethostname()
    port = 2527

    balance = 100

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))
            try:
                print(str(int(data)))
            except ValueError:
                continue
            if(data != 0):
                balance += int(data)
            conn.send(str(balance).encode())  


if __name__ == '__main__':
    server_program()