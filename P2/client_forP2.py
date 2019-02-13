# PROGRAMMING OUR FIRST CLIENT

import socket
from seq_forP2 import Seq
while True:
    # Create a socket for communicating with the server
    s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)

    print("socket created")

    PORT = 8080
    IP = "212.128.253.85"

    # connect to the server
    s.connect((IP, PORT))

    mystr = input("sequence:")
    s1 = Seq(mystr)
    s2 = s1.complement()
    s3 = s2.reversed()
    bases = "A", "C", "T", "G"
    sequences = s1, s2, s3
    nsequences = 0
    s.send(str.encode(s3.strbases))

    msg = s.recv(2048).decode("utf-8")
    print("Sequence is received")
    print(msg)

    s.close()

    print("The end")
