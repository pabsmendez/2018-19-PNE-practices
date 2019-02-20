import socket
from seq_P3 import Seq

# Configure the Server's IP and PORT
PORT = 8087
IP = "212.128.253.111"
MAX_OPEN_REQUESTS = 5


def process_client(cs):

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print("Request message: {}".format(msg))
    msg = msg.split()
    print(msg)
    seq = Seq(msg[0])

    #split investigar luego es poner el 0 en los if in dentro el 2
    listamsg = msg[1:]
    print(listamsg)
    bases = 'A', 'C', 'T', 'G'
    results = []
    if len(msg) > 1:
        for element in listamsg:
            if element == 'len':
                results.append(seq.len())
            elif element == 'complement':
                results.append(seq.complement().strbases)
            elif element == 'reversed':
                results.append(seq.reversed())
            elif element == 'count{}'.format(bases):
                results.append(seq.count(bases))
            elif element == 'percentage':
                results.append(seq.percentage(bases))
    else:
        if msg[0] == 'EXIT':
            cs.close()
            return False
        else:
            cs.send(str.encode("ALIVE"))
            cs.close()
            return True



    # Send the msg back to the client (echo)
    cs.send(str.encode(str(results)))
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
while True:

    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    if not process_client(clientsocket):
        ready = False

    clientsocket.close()