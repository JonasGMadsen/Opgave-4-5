from socket import *
import json

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

operation = input("Enter operation (Random/Add/Subtract): ").strip()

request = {}
if operation == "Random":
    min_num = int(input("Enter the minimum number: "))
    max_num = int(input("Enter the maximum number: "))
    request["operation"] = operation
    request["numbers"] = [min_num, max_num]
elif operation in ["Add", "Subtract"]:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    request["operation"] = operation
    request["numbers"] = [num1, num2]
else:
    print("Invalid operation")
    clientSocket.close()
    exit()

clientSocket.sendall(json.dumps(request).encode())

response_data = clientSocket.recv(1024).decode()
response = json.loads(response_data)
result = response.get("result", "Invalid response")
print(f"Result: {result}")

clientSocket.close()