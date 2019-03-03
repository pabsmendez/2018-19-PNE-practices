import socket
import termcolor

# Change this IP to yours!!!!!
IP = "192.168.56.1"
PORT = 8000
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print()
    print("Request message: ")
    print(msg)
    termcolor.cprint(msg, 'blue')

    url = msg.split("\n")[0]
    try:
        request = url.split()[1]
    except IndexError:
        cs.close()
        return

    if "blue" in request:
        f = open("blue.html", "r")
        content = f.read()
        f.close()
    elif "pink" in request:
        f = open("pink.html", "r")
        content = f.read()
    elif "/" == request:
        f = open("indexP4.html", "r")
        content = f.read()
        f.close()
    else:
        f = open("error.html")
        content = f.read()
        f.close()
    print(request)
    status_line = "HTTP/1.1 200 OK\r\n"

    header = "Content-Type: text/html\r\n"
    header += "Content-length: {}\r\n".format(len(str.encode(content)))

    reponse = status_line + header + "\r\n" + content

    cs.send(str.encode(reponse))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)