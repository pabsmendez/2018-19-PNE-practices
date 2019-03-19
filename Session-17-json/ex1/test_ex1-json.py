import json
import termcolor

# -- open json file
file = open("person_ex1.json", "r")

# -- held info of the file inside the variable
person = json.load(file)

print()
termcolor.cprint("total people in data base: {}".format(len(person["People"])))
for j in person["People"]:
    termcolor.cprint("Name: ", 'green', end= '')
    print(j["name"])
    termcolor.cprint("Age: ", 'green', end= '')
    print(j["age"])

    for i,num in enumerate(j["Phonenumber"]):
        termcolor.cprint("phone {}".format(i), end= '')
        termcolor.cprint("      Type: ", 'red', end= '')
        print(num['type'])
        termcolor.cprint("      Number: ", 'red', end='')
        print(num['number'])