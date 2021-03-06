import socket

# SERVER IP, PORT
IP = "192.168.56.1"
PORT = 8000

# Before connecting to the server, ask the user for the string
msg = """ACTG
countA
countT
percentageG
reversed
complement
"""

# Now we can create the socket and connect to the servewr
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (results.append(IP, PORT)
s.connect((IP, PORT))
# Send the request message to the server
s.send(str.encode(msg))

# Receive the servers respoinse
response = s.recv(2048).decode()

# Print the server's response
print(response)

s.close()