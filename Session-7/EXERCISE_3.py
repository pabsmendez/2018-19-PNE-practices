# PROGRAMMING OUR FIRST CLIENT
import socket

while True:
    # Create a socket for communicating with the server
    s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)

    print("socket created")

    PORT = 8080
    IP = "212.128.253.88"

    # connect to the server
    s.connect((IP, PORT))


    s.send(str.encode(("please enter a message")))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER")
    print(msg)

print("The end")
