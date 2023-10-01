import json
from socket import *
import concurrent.futures
import random

# Shadows name from outer scoper?


def handle_client(connectionSocket, client_address):
    print('Connection established with', client_address)
    data = connectionSocket.recv(1024).decode()
    request = json.loads(data)

    operation = request.get("operation")
    response = {}

    if operation == "Random":
        min_num = request.get("min")
        max_num = request.get("max")
        result = random.randint(min_num, max_num)
        response["result"] = result
    elif operation == "Add":
        num1 = request.get("num1")
        num2 = request.get("num2")
        result = num1 + num2
        response["result"] = result
    elif operation == "Subtract":
        num1 = request.get("num1")
        num2 = request.get("num2")
        result = num1 - num2
        response["result"] = result
    else:
        response["error"] = "Invalid operation"

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
