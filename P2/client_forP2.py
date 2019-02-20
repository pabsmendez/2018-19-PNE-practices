# PROGRAMMING OUR FIRST CLIENT

import socket
from seq_forP2 import Seq
while True:
    # Create a socket for communicating with the server
    s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)

    print("socket created")

    PORT = 8089
    IP = "212.128.253.111"

    # connect to the server
    s.connect((IP, PORT))

    mystr = input("sequence:")
    s.send(str.encode(mystr))

    msg = s.recv(2048).decode("utf-8")
    print("Sequence is received")
    print(msg)

    s.close()

    print("The end")
