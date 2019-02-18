# PROGRAMMING OUR FIRST CLIENT

import socket

# Create a socket for communicating with the server
s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)

print("socket created")

PORT = 8080
IP = "192.168.56.1"

# connect to the server
s.connect((IP, PORT))

mystr = input("sequence:")
bases = "A", "C", "T", "G"
s.send(str.encode(mystr))

msg = s.recv(2048).decode("utf-8")
print("Sequence is received")
print(msg)

s.close()

print("The end")