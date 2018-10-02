# -*- coding: utf-8 -*-
from shutil import copyfile
import os

folder = "/home/tsuki/aozorabunko/cards/"

print(os.listdir(folder))

subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]

print(subfolders)

for subfolder in subfolders:
    dir_name = subfolder+'/files/'
    print(dir_name)
    print(os.path.exists(dir_name))
    if os.path.exists(dir_name):
        subfiles = [f for f in os.listdir(subfolder+'/files/') if f.endswith('.html')]
        print(subfiles)
        for subfile in subfiles:    
            file_name = subfolder+'/files/'+subfile
            save_name = 'books/'+subfile
            print(file_name)
            copyfile(file_name, save_name)
print('copy done')

