# Example of getting information about the weather of
# a location

import http.client
import json

# -- this function find the correct city woeid
def connection(city):
    try:
        # -- API information
        HOSTNAME = "www.metaweather.com"
        ENDPOINT = "/api/location/search/?query="
        ENDPOINT = ENDPOINT + city

        METHOD = "GET"

        # -- Here we can define special headers if needed
        headers = {'User-Agent': 'http-client'}

        # -- Connect to the serversession-19/exercise-2/metaweather.py:18
        # -- NOTICE it is an HTTPS connection!
        # -- If we do not specify the port, the standar one
        # -- will be used
        conn = http.client.HTTPSConnection(HOSTNAME)

        # -- Send the request. No body (None)
        # -- Use the defined headers
        conn.request(METHOD, ENDPOINT, None, headers)

        # -- Wait for the server's response
        r1 = conn.getresponse()

        # -- Read the response's body and close
        # -- the connection
        text_json = r1.read().decode("utf-8")
        conn.close()

        i = json.loads(text_json)
        return i[0]["woeid"]
    except:
        return False

HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/"
city = input("Introduce the city name: ")
if not (connection(city)):
    print("you introduced an incorrect city name, try again")
else:
    LOCATION_WOEID = str(connection(city))
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
    conn.request(METHOD, ENDPOINT + LOCATION_WOEID + '/', None, headers)

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
    # -- Optionally you can print the
    # -- received json file for testing
    # print(text_json)

    # -- Generate the object from the json file
    weather = json.loads(text_json)

    # -- Get the data
    time = weather['time']

    temp0 = weather['consolidated_weather'][0]
    description = temp0['weather_state_name']
    temp = temp0['the_temp']
    place = weather['title']



    print()
    print("Place: {}".format(place))
    print("Time: {}".format((time).split('T')[1].split('+')[0][:11]))
    print("Sunset: {}".format((weather['sun_set']).split('T')[1].split('+')[0][:11]))
    print("Current temp: {} degrees".format(round(temp, 2)))