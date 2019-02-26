import socket
from seq_P3 import Seq

# Configure the Server's IP and PORT
PORT = 8008
IP = "212.128.253.107"
MAX_OPEN_REQUESTS = 5


def process_client(cs):

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print("Request message: {}".format(msg))

    msg = msg.split()
    seq = Seq(msg[0].upper())

    listmsg = msg[1:]
    results = []
    bases = 'A', 'C', 'T', 'G'
    valid = str(bases)
    counter = 0
    errorcount = 0
    # To search an error
    for i in msg[0].upper():
        if i in valid:
            counter += 1
        elif i not in valid:
            errorcount += 1
    if len(msg[0].upper()) == counter:
        results.append("OK")
    else:
        results.append("ERROR")

    if len(msg) > 1:
        for element in listmsg:
            print(element)
            if element == 'len':
                results.append(str(seq.len()))
            elif element == 'complement':
                results.append(seq.complement().strbases)
            elif element == 'reversed':
                results.append(seq.reversed().strbases)
            elif 'count' in element:
                bases = element[-1].upper()
                if element[-1].upper() in valid:
                    results.append(str(seq.count(bases)))
                else:
                    cs.send(str.encode("ERROR"))
                    cs.close()
                    return True
            elif 'percentage' in element:
                bases = element[-1].upper()
                if element[-1].upper() in valid:
                    results.append(str(seq.percentage(bases)))
                else:
                    cs.send(str.encode("ERROR"))
                    cs.close()
                    return True
            elif element != Seq:
                cs.send(str.encode("ERROR"))
                cs.close()
                return True

    elif len(msg) == 1:
        if seq.strbases == 'EXIT' or seq.strbases == 'exit':
            print("Closed")
            cs.close()
            return False
        elif seq.strbases == "EMPTY":
            cs.send(str.encode("ALIVE"))
            cs.close()
            return True

    results = "\n".join(results)

    # Send the msg back to the client (echo)
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