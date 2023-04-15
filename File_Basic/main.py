import os

current_file = os.path.realpath('10_File_io_Basic_Concepts.ipynb')  
print('current file: {}'.format(current_file))
# Note: in .py files you can get the path of current file by __file__

current_dir = os.path.dirname(current_file)  
print('current directory: {}'.format(current_dir))
# Note: in .py files you can get the dir of current file by os.path.dirname(__file__)

data_dir = os.path.join(os.path.dirname(current_dir), 'data')
print('data directory: {}'.format(data_dir))