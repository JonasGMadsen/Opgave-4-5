import json
from socket import *
import concurrent.futures
import random

# Shadows name from outer scoper?


def handle_client(connectionSocket, client_address):
    print('Connection established with', client_address)
    request_data = connectionSocket.recv(1024).decode()
    request = json.loads(request_data)

    operation = request.get("operation")
    numbers = request.get("numbers", [])

    if operation == "Random":
        min_num, max_num = map(int, numbers)
        result = random.randint(min_num, max_num)
    elif operation == "Add":
        num1, num2 = map(int, numbers)
        result = num1 + num2
    elif operation == "Subtract":
        num1, num2 = map(int, numbers)
        result = num1 - num2
    else:
        result = "Invalid operation or numbers"

    response = {"result": result}
    connectionSocket.sendall(json.dumps(response).encode())
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
