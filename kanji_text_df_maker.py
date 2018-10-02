import pandas as pd
import numpy as np
from collections import Counter


'''
Convert df which has
text  author dict 
----------------

to

text author kanji1 kanji2 kanji3 ...
'''


class Kanji_text_df_maker:
    
    
    
    def __init__(self,df):
        self.all_kanji = {} #all kanji, with values corresponding to total numbers
        self.df_kanjied = df.copy()
        self.n_text = len(df)

        for d in df['kanji']:
            #print(d)
            self.all_kanji = Counter(self.all_kanji) + Counter(d)
            
        for k in self.all_kanji:
            self.df_kanjied[k] = np.zeros(self.n_text)
            
        temp_dict = {}
        print(df.dtypes)



        for ind in range(self.n_text):
            temp_dict = df['kanji'].iloc[ind][0]
            print(temp_dict)
            for k in temp_dict:
                df[k][ind] = temp_dict[k]
                
                    
        print(self.df_kanjied)
            
            
            
  
               
            
    def print_all_kanji(self):
        print(self.all_kanji)
        print(self.kanji_occurences)
        
        
if __name__ == '__main__':
    fName = 'training.csv'
    df = pd.read_csv(fName)

    print(df.columns)

    ktool = Kanji_text_df_maker(df)
    #ktool.print_all_kanji()
