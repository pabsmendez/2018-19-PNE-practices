# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
import termcolor

PORT = 8000
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
people = json.loads(data1)

# Print the information in the object
print()
termcolor.cprint("total people in data base: {}".format(len(people["People"])))
for j in people["People"]:
    termcolor.cprint("Name: ", 'green', end="")
    print(j['name'])
    termcolor.cprint("Age: ", 'green', end="")
    print(j['age'])
    # Print all the numbers
    for i, num in enumerate(j["Phonenumber"]):
        termcolor.cprint("  Phone {}:".format(i), 'blue')
        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])