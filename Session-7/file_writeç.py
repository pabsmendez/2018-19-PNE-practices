# Example of reading a file located
# In our local filesystem

NAME = "mynotes.txt"

# Open the file
myfile = open(NAME, 'r')

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("the file contents are: {}".format(contents))

myfile.close()

f = open(NAME, 'a')
f.write("THIS IS A TEXT EXAMPLE TO ADDING TO MY FILE")
f.close()
print("the end")
