#!/usr/bin/python3
import socket

#server initialization, Creating the socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reuse socket

#host = 'IP ADDRESS'
host = socket.gethostbyname() #Host is the server IP
port = 444  

#Binding to socket
serverSocket.bind((host, port)) #Host will be replaced/substitued with IP

#Starting TCP listener
serverSocket.listen(5)

while True:
    #Starting the connection 
    clientSocket, addr = serverSocket.accept()
    print("Connection received from %s " % str(addr))

    #Message sent to client after successful connection
    msg = 'Thank you for connecting ' + "\r\n"
    clientSocket.send(msg.encode('ascii'))

    clientSocket.close()


