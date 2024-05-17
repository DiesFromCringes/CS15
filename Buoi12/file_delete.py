import os
import shutil
src = 'D:\\CS15\\b\\b.txt'

#Xoa File
try:
    os.remove(src)
except FileNotFoundError:
    print('File Not Found!')
else:
    print('File is deleted')

#Xoa folder
path_dir = 'D:\\CS15\\b'
try:
    os.rmdir(path_dir)
except FileNotFoundError:
    print('Folder not found!')
except PermissionError:
    print('You do not have permission')
except OSError:
    print('You do not have permission')
    shutil.rmtree(path_dir)
    print('Deleted files and folder')
else:
    print('Folder is deleted')  