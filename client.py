# Name:     Piam Pan Ya Chittisane
# UARK ID:  010868460

import socket


def menu():
    host = socket.gethostname()
    port = 2527

    client_socket = socket.socket()
    client_socket.connect((host, port))

    menuContinue = 1
    while(menuContinue != 0):
        print("")
        print("==================================")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("0. Exit")
        try:
            menuContinue = int(input("Type the number for the action you want to do: "))
        except ValueError:
            print("Not an integer. Try again.")
        if(menuContinue == 1):
            depositRequest(client_socket)
            input("Press enter to continue")
        elif(menuContinue == 2):
            withdrawRequest(client_socket)
            input("Press enter to continue")
        elif(menuContinue == 3):
            balanceRequest(client_socket)
            input("Press enter to continue")
        elif(menuContinue == 0):
            client_socket.shutdown(socket.SHUT_RDWR)
            quit()
        else:
            print("Invalid input. Try again.")

def depositRequest(client_socket):
    balance = balanceRequest(client_socket)

    depositAmount = -1
    while (depositAmount < 0):
        try:
            depositAmount = int(input("How much would you like to deposit? : $"))
        except ValueError:
            print("Not an integer. Try again.")
    
    client_socket.send(str(depositAmount).encode())
    balance = client_socket.recv(1024).decode()

    print('Current Balance: $' + balance)
    return

def withdrawRequest(client_socket):
    balance = balanceRequest(client_socket)

    if(int(balance) == 0):
        print("Cannot withdraw. No money in account.")
        return

    withdrawAmount = -1
    while (withdrawAmount < 0 or withdrawAmount > int(balance)):
        try:
            withdrawAmount = int(input("How much would you like to withdraw? : $"))
        except ValueError:
            print("Not an integer. Try again.")
    
    client_socket.send(str(-withdrawAmount).encode())
    balance = client_socket.recv(1024).decode()

    print('Current Balance: $' + balance)
    return

def balanceRequest(client_socket):
    client_socket.send(str(0).encode())  # send 0
    balance = client_socket.recv(1024).decode()  # retrieve current balance

    print('Current Balance: $' + balance)
    return balance

if __name__ == '__main__':
    menu()