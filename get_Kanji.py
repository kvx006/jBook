# -*- coding: utf-8 -*-
import re
import sys
import os
from collections import Counter

## UNICODE BLOCKS ##

# Regular expression unicode blocks collected from 
# http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/

hiragana_full = r'[ぁ-ゟ]'
katakana_full = r'[゠-ヿ]'
kanji = r'[㐀-䶵一-鿋豈-頻]'
radicals = r'[⺀-⿕]'
katakana_half_width = r'[｟-ﾟ]'
alphanum_full = r'[！-～]'
symbols_punct = r'[、-〿]'
misc_symbols = r'[ㇰ-ㇿ㈠-㉃㊀-㋾㌀-㍿]'
ascii_char = r'[ -~]'

## FUNCTIONS ##

def extract_unicode_block(unicode_block, string):
    ''' extracts and returns all texts from a unicode block from string argument.
        Note that you must use the unicode blocks defined above, or patterns of similar form '''
    return re.findall( unicode_block, string)

def remove_unicode_block(unicode_block, string):
    ''' removes all chaacters from a unicode block and returns all remaining texts from string argument.
        Note that you must use the unicode blocks defined above, or patterns of similar form '''
    return re.sub( unicode_block, '', string)

def get_all_kanji(text):
    kanji_list = extract_unicode_block(kanji, text)
    #print(kanji_list)
    return kanji_list
    #other_list = ['初', '嫌']

    #print(set(kanji_list).intersection(other_list))
    
def main():
    fName = sys.argv[1]
    with open(fName, 'r') as myfile:
        data = myfile.read().replace('\n','')
        kanjis = get_all_kanji(data)
    kanji_counts = Counter(kanjis)

        
    root, ext = os.path.splitext(fName)
    with open(root+'_kanji.csv', 'w') as myfile:
        for key, value in kanji_counts.most_common():
            myfile.write(str(key)+","+ str(value)+ "\n")

if __name__ == "__main__":
    main()
