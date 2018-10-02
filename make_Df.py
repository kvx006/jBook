import csv
import pandas as pd
import glob, os


def get_file_Data(fName):
    with open(fName, 'r') as f:
            read_data = f.read().split("\n")


    #print(read_data)
    read_data = read_data[:-1]
    read_data[0] = read_data[0]
    #print(read_data)
    return read_data
    
    
def main():
    #os.chdir()
    df = pd.DataFrame([], columns=['loc','title', 'author'])
    for myFile in glob.glob("*.csv"):
        new_entry = get_file_Data(myFile)
        df.loc[len(df)] = new_entry
    df.to_csv('meta_data_author_books.csv')
    print('Done')

if __name__ =="__main__":
    main()

