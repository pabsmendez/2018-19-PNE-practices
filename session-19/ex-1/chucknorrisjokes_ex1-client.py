# Accessing to the Chuck Norris jokes service for getting an URL
# of a random joke of Chuck Norris. This clients just print it on
# the console

import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/count", "/jokes/random", "/categories"
METHOD = "GET"
# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standard one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
for ENDPOINTS in ENDPOINT:
    conn.request(METHOD, ENDPOINTS, None, headers)

    # -- Wait for the server's response/categories
    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Optionally you can print the
    # -- received json file for testing
    # print(text_json)

    # -- Generate the object from the json file
    chuck = json.loads(text_json)
    i = chuck['value']

    # -- Print the received URL
    if ENDPOINTS == "/jokes/count":
        print("number of jokes: ", chuck['value'])
    elif ENDPOINTS == "/categories":
        print("number of categories: ", len(chuck['value']))
    elif ENDPOINTS == "/jokes/random":
        print("Cat image: ", chuck['value'])
    else:
        print("not a correct endpoint")