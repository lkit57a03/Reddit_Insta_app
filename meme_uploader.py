from instapy_cli import client
import pandas as pd

username = '7355517759'
password = 'j0y0isgreat'
image    = 'ythcbag3l4r31.jpg'
text     = 'oh boy, here we go again'


def upload_files(image_url, title):
    with client(username, password) as cli:
        return_val = cli.upload(image_url, title)
        print(return_val)
    return return_val['status'] == 'ok' 

def give_un_uploaded_memes(filename= 'memes_data.csv'):
    df = pd.read_csv(filename, index_col='id')


    for index, row in df.loc[df['updated']==False].iterrows():
        upload_files(row['url'], row['title'])
        df.loc[index,'updated'] = True
        break


    print(df.head())
    df.to_csv('memes_data.csv')

    return non_uploaded
    
give_un_uploaded_memes()