# -*- coding: utf-8 -*-

'''
Removes foreign authors 
and authors with unknowns = 'none'
and authors with an unusual number of books which would skew processing
and authors with litle amounts 
'''


import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties
import numpy as np
from collections import Counter

from sklearn.utils import shuffle
import csv

fp = FontProperties(fname=r'/home/tsuki/Downloads/ipagp.ttf', size=14)

def is_foreign_author(author_name):
    print(author_name)
    return re.search('[a-zA-z]',author_name)!=None and author_name!='none'


fName = 'books_converted/meta_data_author_books.csv'
df = pd.read_csv(fName)
df['author'] = df['author'].astype('str') 



df['is_foreign'] = df['author'].apply(is_foreign_author)

uncommon_upper_bound = 100
to_many_lower_bound = 500

df2 = df.groupby('author').filter(lambda x: len(x)>=uncommon_upper_bound and len(x) <=to_many_lower_bound)

df2 = df2[df2['is_foreign'] == False]
df2 = df2[df2['author'] != 'none']
print(df2)

print(len(df))
print(len(df2['author'].value_counts()))
#df2 = df[
#df.to_csv(fName)


font = {'family' : 'TakaoGothic'}
matplotlib.rc('font', **font)

df2['author'].value_counts()[:30].plot(kind='barh')

plt.ylabel('作家',fontproperties=fp)

plt.savefig('author_counts.png')
plt.close()


df2.to_csv('common_authors.csv')
print(len(df2['title'].value_counts()))


df2 = shuffle(df2)

path = 'kanji/'
dict_list = []
all_kanji = {}
for ind in range(len(df2['title'])):
    fileName = df2.iloc[ind]['loc']+'_kanji.csv'
    print(ind, fileName)
    reader = csv.reader(open(path+fileName, 'r'))
    d = {}
    for row in reader:
        k, v = row
        d[k] = int(v)
    dict_list.append([d])
    all_kanji = Counter(all_kanji) + Counter(d)

for k in all_kanji:        
    df2[k] = np.zeros(len(df2['title']))
    
print('Up to ', len(df2['title']))
for ind in range(len(df2['title'])):
    print(ind)
    for d in dict_list[ind]:
        for k in d:
            #print(d[k])
            df2[k].iloc[ind] = int(d[k])


num_titles = len(df2['title'])
eightyth = int(num_titles*0.8)
df_training = df2[:eightyth]
df_test = df2[eightyth:]


df_training.to_csv('training.csv')
df_test.to_csv('test.csv')



