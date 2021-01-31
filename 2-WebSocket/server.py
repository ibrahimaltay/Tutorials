import socket

server = socket.socket()
IP = 'localhost'
PORT = 65432

server.bind((IP,PORT))
server.listen(1)

client, client_address = server.accept()
print(client_address)

client.send("Welcome to my server!".encode())

server.close()