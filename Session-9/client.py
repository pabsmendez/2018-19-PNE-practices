import socket
import termcolor

# SERVER IP, PORT
IP = "212.128.253.86"
PORT = 8080



while True:

    # Before connecting to the server, ask the user for the string
    msg = input("> ")


    # Now we can create the socket and connect to the servewr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    termcolor.cprint("Response: {}".format(response, 'green'))

    s.close()