from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

operation = input("Enter operation (Random/Add/Subtract): ")
clientSocket.sendall(operation.encode())

if operation == "Random":
    min_num, max_num = map(int, input("Enter minimum and maximum numbers separated by space: ").split())
    clientSocket.sendall(f"{min_num} {max_num}".encode())
elif operation in ["Add", "Subtract"]:
    num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
    clientSocket.sendall(f"{num1} {num2}".encode())
else:
    print("Invalid operation")
    clientSocket.close()
    exit()

result = clientSocket.recv(1024).decode()
print("Result from server:", result)

clientSocket.close()
