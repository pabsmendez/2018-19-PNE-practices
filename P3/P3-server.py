import socket
from seq_P3 import Seq

# Configure the Server's IP and PORT
PORT = 8080
IP = "192.168.56.1"
MAX_OPEN_REQUESTS = 5


def process_client(cs):

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print("Request message: {}".format(msg))

    msg = msg.split()
    seq = Seq(msg[0].upper())

    #split investigar luego es poner el 0 en los if in dentro el 2
    listamsg = msg[1:]
    bases = 'A', 'C', 'T', 'G'
    results = []
    if len(msg) > 1:
        print("OK")
        for element in listamsg:
            print(element)
            if element == 'len':
                results.append(str(seq.len()))
            elif element == 'complement':
                results.append(seq.complement().strbases)
            elif element == 'reversed':
                results.append(seq.reversed().strbases)
            elif 'count' in element:
                bases = element[-1]
                results.append(str(seq.count(bases)))
            elif 'percentage' in element:
                bases = element[-1]
                results.append(str(seq.percentage(bases)))
    else:
        if seq.strbases == 'EXIT':
            print("Closed")
            cs.close()
            return False
        elif seq.strbases == "EMPTY":
            cs.send(str.encode("ALIVE"))
            cs.close()
            return True




    # Send the msg back to the client (echo)
    results = "\n".join(results)
    cs.send(str.encode(results))
    cs.close()
    return True


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