import urllib.request
import pandas as pd
import praw
import csv
import os

reddit = praw.Reddit(client_id='cYutN672JNJ_8Q',client_secret='q0K95MT8tTmyJCIiC35U6D8d7oM',user_agent='Harsh_Tiwari')
# print(reddit.read_only)


def file_exists_or_not_empty(filename):
    filename = os.path.join(os.getcwd(), filename)
    return os.path.isfile(filename) and os.path.getsize(filename) > 0
# print(file_exists_or_is_empty('memes_data.csv'))

with open('memes_data.csv','a+') as memes_file:
    writer = csv.writer(memes_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    does_file_exists =  file_exists_or_not_empty('memes_data.csv')
    
    if not does_file_exists:
        writer.writerow(["id","title","url","score"])    
    if does_file_exists:
        memes_data = pd.read_csv('memes_data.csv')
    
    for sub in reddit.subreddit('memes').hot(limit=20):
        if does_file_exists:
            found = memes_data[memes_data['id'].str.contains(sub.id)]
        else:
            found=[]
        if len(found) == 0:
            meme_data = [sub.id,sub.title,sub.url,sub.score]
            writer.writerow(meme_data)
        else:
            pass
