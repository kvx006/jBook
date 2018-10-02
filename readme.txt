Purpose:
To be able to identify Japanese authors/or time period based on kanji used



Goals:

1. Isolate Kanji from string/text
2. Read text
3. Add in to database? Including author name and year published?
4. Can we predict author or date from Kanji use alone?


Bells and Whistles:
Number of characters in book:: long/short/medium?

May 15: What is good way to get data?
Currently at this step:

http://darthcrimson.org/digital-japanese-literature-aozora-bunko/

Issue with character? <- got

use shiftjis_converter.py to conver from shiftjis to utf-8

May 16: Able to get counts of kanji from a file

May 17: Got all files and converting from shiftjis to utf-8 (skipped some with issues)
Originally 14783 files/books  (Command to count:  \ls -afq | wc -l)
Converted sucessfully 14773 files/books 

Not all files are formulated with same html format, cant get author/title 
e.e file 
2387.html

Some files didn't have 底本 keyword so skip

Useful for counting files by type:
ls | awk -F . '{print $NF}' | sort | uniq -c | awk '{print $2,$1}'



May 18: Getting all kanji and counts into kanji_convert

May 20: Making meta-data dataframe ::make_df.py
Able to identify foreign authors; and have most common authors:

May 21: Getting most common authors

Japanese font:
Use 
# -*- coding: utf-8 -*-
import matplotlib
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'/home/tsuki/Downloads/ipagp.ttf', size=14)
font = {'family' : 'TakaoGothic'}
matplotlib.rc('font', **font)
plt.ylabel('作家',fontproperties=fp)


May 23: 
Prepared the data for processing; split into training and testing

Next step: for each author, find location, open location.kanji, read, and append to list, compactify list
=>
author, kanji_dict (kanji, freq) Check



Aug 13:
Figuring out what to do:
Try Naive-Bayes approach first;
Document results once done.
https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a


Try and use other tools?




Naive Bayes procedure:
In df, given a dictionary from each book, 



Idea:
For each book:
    pass in kanji dict
    create column for tf-idf array/dict?
    for each character in kanji dict:
        do character freq/all freq * 





