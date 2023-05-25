# Python Program to Copy One File to Another File
import os
# Take the input file
input_file= os.path.realpath('file.txt')
file_open= open(input_file,"r")

output_file= "copy_text.txt"
if not os.path.exists(output_file):
    file_write= open(output_file, "w")
else:
    file_write= open(output_file,"w")
    print("File exixts")

with file_open as file:
    with file_write as file1:
        for line in file:
            file1.write(line)

file_open.close()
file_write.close()

# Verify the content of the files
with open(input_file, "r") as file:
    print(file.read())
print('+++++++++++++++++++++++++++++++++')
with open(output_file, "r") as file1:
    print(file1.read())


       


