# opening a file
greetings = open("hello.txt", "r")
print(greetings)
greetings.close()

#file properties
f = open("hello.txt", "r")
print("filename: ", f.name)
print("filemode: ", f.mode)
print("Is file closed?: ", f.closed) #false
f.close()
print("Is file closed?: ", f.closed) # true

# reading a file
f = open("hello.txt", "r")
contents = f.read()
print(contents)
f.close()

