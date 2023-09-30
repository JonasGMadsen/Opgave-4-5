from socket import *
import concurrent.futures
import random

# Shadows name from outer scoper?


def handle_client(connectionSocket, client_address):
    print('Connection established with', client_address)
    operation = connectionSocket.recv(1024).decode()

    if operation == "Random":
        min_num, max_num = map(int, connectionSocket.recv(1024).decode().split())
        result = random.randint(min_num, max_num)
    elif operation == "Add":
        num1, num2 = map(int, connectionSocket.recv(1024).decode().split())
        result = num1 + num2
    elif operation == "Subtract":
        num1, num2 = map(int, connectionSocket.recv(1024).decode().split())
        result = num1 - num2
    else:
        result = "Invalid operation"

    connectionSocket.sendall(str(result).encode())
    connectionSocket.close()


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')

with concurrent.futures.ThreadPoolExecutor() as executor:
    while True:
        connectionSocket, client_address = serverSocket.accept()
        executor.submit(handle_client, connectionSocket, client_address)
