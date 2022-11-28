import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    menuContinue = 1
    while(menuContinue != 0):
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("0. Exit")
        try:
            menuContinue = int(input("Type the number for the action you want to do: "))
        except ValueError:
            print("Not an integer. Try again.")
        if(menuContinue == 1):
            deposit(client_socket)
        if(menuContinue == 2):
            withdraw(client_socket)
        if(menuContinue == 3):
            check(client_socket)
        elif(menuContinue == 0):
            client_socket.close()
            quit()
        else:
            print("Invalid input. Try again.")

def deposit(client_socket):
    message = "d"
    
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: ' + data)  # show in terminal

    message = input(" -> ")  # again take input
    return

def withdraw(client_socket):
    return

def check(client_socket):
    return

if __name__ == '__main__':
    client_program()