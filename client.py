#!/usr/bin/python3

import socket

#Initialization, Create socket object
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = 'IP_ADDRESS'
host = socket.gethostname()

port = 444

clientSocket.connect((host, port)) # substitue the host with the server IP

#Receiving a maximum of 1024 bytes
msg = clientSocket.recv(4064)

clientSocket.close()

print(msg.decode('ascii'))