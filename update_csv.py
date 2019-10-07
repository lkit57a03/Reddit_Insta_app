import pandas as pd
import csv
import os

import memes_dowloader

def file_exists_or_not_empty(filename):
    filename = os.path.join(os.getcwd(), filename)
    return os.path.isfile(filename) and os.path.getsize(filename) > 0

def initialize_file(filename= 'memes_data.csv'):
    with open(filename,'w+') as memes_file:
        writer = csv.writer(memes_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        does_file_exists =  file_exists_or_not_empty(filename)
        if not does_file_exists:
            writer.writerow(["id","title","url","score","updated"])

def write_memes_to_file(memes_list, filename = 'memes_data.csv'):
    if not file_exists_or_not_empty(filename):
        initialize_file(filename=filename)

    with open(filename,'a+') as memes_file:
        writer = csv.writer(memes_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        memes_data = pd.read_csv(filename)
        for item in memes_list:
            found = memes_data[memes_data['id'].str.contains(item['id'])]
            if (len(found) == 0):
                writer.writerow([item['id'], item['title'], item['url'], item['score'], item['uploaded']])
            else:
                pass



memes_list = memes_dowloader.get_posts()      
write_memes_to_file(memes_list=memes_list)  
        
