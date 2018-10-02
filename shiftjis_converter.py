import os
import codecs
            
folder = "books"

print(os.listdir(folder))

subfiles = [f.path for f in os.scandir(folder) if f.is_dir()]

for subfile in subfiles:    
    file_name = 'books/'+subfile
    save_name = 'books/'+subfile
    print(save_name)

    with codecs.open(file_name, mode='r', encoding='shiftjis') as file:
        lines = file.read()

    with codecs.open(save_name, mode='w') as file:
        for line in lines:
            file.write(line)
