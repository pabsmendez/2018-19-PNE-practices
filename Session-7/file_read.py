# Example of reading a file located
# In our local filesystem

NAME = "mynotes.txt"

# Open the file
myfile = open(NAME, 'r')

print("File oprned: {}".format(myfile.name))

contents = myfile.read()

print("the file contents are: {}".format(contents))
