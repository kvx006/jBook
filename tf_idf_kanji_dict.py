import pandas as pd
import numpy as np
from collections import Counter


'''
How to implement a tf-idf
Next get weighting function down

Tf-idf associates a number to each word, then we use what?
idf will essentially remove stop words
'''


class Kanji_dict_tf_idf:
    
    
    
    def __init__(self,df):
        self.total_nums = len(df)
        self.all_kanji = {} #all kanji, with values corresponding to total numbers
        self.kanji_occurences = {} #number of texts in which kanji occur
        self.kanji_idf = {}
        #create idf by doing -log(kanji_occurences/N=total number of texts=length of df)
        # tf-idf = tf * idf
        
        for d in df['kanji']:
            self.all_kanji = Counter(self.all_kanji) + Counter(d)
            
            self.kanji_idf[key] = 0
            for d in df['kanji']:
                if key in  d:
                     self.kanji_occurences[key]+=1
     
        for k,v in kanji_occurences:
            self.kanji_idf[k] = -np.log(self.kanji_occurences[k]/self.total_nums)     
            
            
            
  
               
            
    def print_all_kanji(self):
        print(self.all_kanji)
        print(self.kanji_occurences)
