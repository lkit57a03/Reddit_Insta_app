from instapy_cli import client
import pandas as pd
import time

username = '7355517759'
password = 'j0y0isgreat'


def upload_files(username, password, image_url, title):
    with client(username, password) as cli:
        print(image_url, title)
        return_val = cli.upload(image_url, title)
        print(return_val)
    return return_val['status'] == 'ok' 

def check_for_non_uploaded_and_upload(username, password,subreddit_name='meme'):
    filename = 'data/{}_data.csv'.format(subreddit_name)
    df = pd.read_csv(filename, index_col='id')
    print(username, password)

    counter = 0
    for index, row in df.loc[df['updated']==False].iterrows():
        if row['url'].endswith('.jpg'):
            return_value = upload_files(username, password, row['url'], row['title'])
            time.sleep(60*10)
            if counter >= 5:
                break
        else:
            return_value = 0
        df.loc[index,'updated'] = True

    print(df.head())
    df.to_csv(filename)
    return return_value
