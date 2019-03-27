# Example of getting information stored in github

import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/", "/repos/"
GITHUB_ID = input("name in github: ")
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT[0] + GITHUB_ID, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

conn.request(METHOD, ENDPOINT[1] + GITHUB_ID + '/2018-19-PNE-practices/commits', None, headers)

# -- Wait for the server's response
r2 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r2.status, r2.reason)

# -- Read the response's body and close
# -- the connection
text_json2 = r2.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)
conn.request(METHOD, ENDPOINT[0] + GITHUB_ID + '/repos', None, headers)

# -- Wait for the server's response
r3 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r2.status, r2.reason)

# -- Read the response's body and close
# -- the connection
text_json3 = r3.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
user = json.loads(text_json)
user2 = json.loads(text_json2)
user3 = json.loads(text_json3)
# -- Get some data
login = user['login']
name = user['name']
bio = user['bio']
nrepos = user['public_repos']
# -- to find the repositories name
list_of_repositories = []
for i in user3:
    repo_name = i['name']
    list_of_repositories.append(repo_name)

print()
print("User: {}".format(login))
print("Name: {}".format(name))
print("Name of repositories", list_of_repositories)
print("Number of commits", len(user2))
