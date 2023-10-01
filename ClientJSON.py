import json
from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

operation = input("Enter operation (Random/Add/Subtract): ")

request = {"operation": operation}

if operation == "Random":
    min_num, max_num = map(int, input("Enter minimum and maximum numbers separated by space: ").split())
    request["min"] = min_num
    request["max"] = max_num
elif operation in ["Add", "Subtract"]:
    num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
    request["num1"] = num1
    request["num2"] = num2
else:
    print("Invalid operation")
    clientSocket.close()
    exit()

clientSocket.sendall(json.dumps(request).encode())
response_data = clientSocket.recv(1024).decode()
response = json.loads(response_data)

if "error" in response:
    print("Error:", response["error"])
else:
    print("Result from server:", response["result"])

clientSocket.close()
