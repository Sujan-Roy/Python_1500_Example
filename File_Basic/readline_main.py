input_file= open("file.txt","r")
# Read the whole text at a time
#print(input_file.read())

# Read the file line of  text at a time
print(input_file.readline())

input_file.close()
