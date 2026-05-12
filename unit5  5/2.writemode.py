# Writing a file
newFile = open("2.newFile.txt", "w")
print(newFile)
newFile.write("This is a new file created by python.")
newFile.close()

FileOverwrite = open("2.newFile.txt", "w")
FileOverwrite.write("The content of the newFile is now changed.")
FileOverwrite.close()

# append a file
appendFile = open("hello.txt", "a")
appendFile.write("\n\nDon't forget to smile today!")
appendFile.close()

#with statement
with open("hello.txt", "r") as f:
    contents = f.read()
    print(contents)
