import socket
import sys
import termcolor
# Configure the Server's IP and PORT
PORT = 8082
IP = "212.128.253.111"
MAX_OPEN_REQUESTS = 5


def process_client(cs):

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print("Request message: {}".format(termcolor.cprint(msg, 'green')))

    if msg == "EXIT":
        cs.close()
        return False


    # Send the msg back to the client (echo)
    cs.send(str.encode(msg))
    cs.close()

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

ready = True
while ready:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    if not process_client(clientsocket):
        ready = False

    clientsocket.close()