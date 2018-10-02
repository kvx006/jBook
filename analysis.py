# -*- coding: utf-8 -*-

import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties
import numpy as np
from sklearn.utils import shuffle
import csv

#import tf_idf_kanji_dict as kanji_tool

'''
Kanji character starts from column 6-5689

P(author | text) = P(text | author)P(author)/P(text)
which is

P(author | character) = P(character | author)P(author)/P(character)
Possible issues include Probabilities being small?

Obtained P(author) and P(character)

Now need P(character | author)

for each author in df:
    author_character_count+= char count
    
    
But now how to use test data?

'''




fName = 'training.csv'

df = pd.read_csv(fName)


num_works = len(df['author'])

''' Considering all Kanji, and count'''
kanji_s = df.columns.tolist()
kanji_s = kanji_s[6:]
kanji_totals = {}
for kanji in kanji_s:
    kanji_totals[kanji] = df[kanji].sum()
total_kanji_used = sum(kanji_totals.values())


''' Probability of the Kanji appearing, throughout all texts
    Might be useful to determine which words are not useful as very common words => less information
    Explore idea later on with TFIDF
'''
num_unique_kanji = len(kanji_totals)
kanji_prob = {}
for kanji in kanji_s:
    kanji_prob[kanji] = kanji_totals[kanji]/total_kanji_used
    
author_counts = dict(df['author'].value_counts())
author_prob = {}


''' How many works are written by the author'''
for author, counts in author_counts.items():
    author_prob[author] = int(counts)/num_works


df2 = df.groupby('author').agg('sum')

df2['total_character_used'] = df2.iloc[:,3:].sum(axis=1)
for ind in range(3,num_unique_kanji):
    df2.iloc[:,ind] = df2.iloc[:,ind]/df2['total_character_used']
print(df2)



_counts/num_works
#print(author_probability)

