import socket

server = socket.socket()
IP = 'localhost'
PORT = 65432

server.connect((IP,PORT))
print("Connection Successful")

message = server.recv(1024)
print(message.decode())
server.close()
