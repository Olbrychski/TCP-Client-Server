import socket
import threading

N = 5  # max number of clients

# Server initialization
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 1234))
server.listen()



clientsConnected = set()
ranks = {}



