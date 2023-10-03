from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

operation = input("Enter operation (Random/Add/Subtract): ")

if operation == "Random":
    min_num = input("Enter the minimum number: ")
    max_num = input("Enter the maximum number: ")
    clientSocket.sendall(f"{operation} {min_num} {max_num}".encode())
elif operation in ["Add", "Subtract"]:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    clientSocket.sendall(f"{operation} {num1} {num2}".encode())
else:
    print("Invalid operation")
    clientSocket.close()
    exit()

response = clientSocket.recv(1024).decode()
print(f"Result: {response}")

clientSocket.close()


