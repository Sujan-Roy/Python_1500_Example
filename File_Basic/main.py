import os

current_file = os.path.realpath('file3.txt')  
print('current file: {}'.format(current_file))


current_dir = os.path.dirname(current_file)  
print('current directory: {}'.format(current_dir))
# Note: in .py files you can get the dir of current file by os.path.dirname(__file__)
file_Open = open(current_file,"r")
print(file_Open.read())
file_Open.close()
