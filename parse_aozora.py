# -*- coding: utf-8 -*-
import os
import glob 
import sys
from bs4 import BeautifulSoup
from tinysegmenter import *

for filename in glob.iglob('*.html'):

# Remove ruby and <rt> <rp> tags from text

    with open(filename, 'r') as f:
        input = f.read()
    print(filename)

    soup = BeautifulSoup(input)
    tagname = 'rt'
    for tag in soup.findAll(tagname):
        tag.extract()

    tagname = 'rp'
    for tag in soup.findAll(tagname):
        tag.extract()
    
    tagname = 'span'
    for tag in soup.findAll(tagname):
    	tag.extract()
    nonruby = str(soup)
    
    

# Remove all HTML tags and attributes, then write the file to (filename).txt

    nonruby = re.sub('<[^<]+?>', '', nonruby)
    
    segmenter = TinySegmenter() 
    
    tokenized = segmenter.tokenize(nonruby)
    
    #print(tokenized.index('底本'))
    
    try:
        tokenized = tokenized[0:tokenized.index('底本')-1]
    
    except ValueError: 
        print('No 底本')
      
    tokenized = ' '.join(tokenized)
    
    root, ext = os.path.splitext(filename)
    
    file1 = open( root+ '.txt', 'w')
    file1.write(tokenized)
    file1.close()
    
    
    title = "none"
    author = "none"
    
    try:
        title = soup.select('h1.title')[0].text.strip()
        print(title)
        author = soup.select('h2.author')[0].text.strip()
        print(author)

    except IndexError:
        print("no title?")
        title = "none"
        author = "none"
        
    file2 = open( root+ '.csv', 'w')
    file2.write(str(root)+"\n")
    file2.write(title+"\n")
    file2.write(author+"\n")
    file2.close()
