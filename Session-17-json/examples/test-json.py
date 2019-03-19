import json
import termcolor

# -- open json file
f = open("person.json", 'r')

# -- held info of the file inside the variable
person = json.load(f)

print()

termcolor.cprint("Name: ", 'green', end= '')
print(person["Firstname"], person["Lastname"])
termcolor.cprint("Age: ", 'green', end= '')
print(person["age"])

for i,num in enumerate(["Phonenumber"]):
    termcolor.cprint("Phone {}".format(i), end= '')

    termcolor.cprint("      Type: ", 'red', end= '')
    print(num['type'])
    termcolor.cprint("      Number: ", 'red', end='')
    print(num['number'])