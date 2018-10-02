import codecs
import os
import glob 

for filename in glob.iglob('*.html'):
    print(filename)

    with codecs.open(filename, mode='r', encoding='shiftjis') as file:
        lines = file.read()

    savename = '../books_converted/' + filename
    with codecs.open(savename, mode='w') as file:
        for line in lines:
            file.write(line)

