from instapy_cli import client
import pandas as pd

username = '7355517759'
password = 'j0y0isgreat'
image    = 'ythcbag3l4r31.jpg'
text     = 'oh boy, here we go again'

# with client(username, password) as cli:
#     return_val = cli.upload("https://i.redd.it/2bud7tc6p3r31.jpg", text)
#     print(return_val)

def upload_files(non_uploaded_df):
    for index, row in non_uploaded_df.iterrows():
        row['updated'] = True

def give_un_uploaded_memes(filename= 'memes_data.csv'):
    df = pd.read_csv(filename, index_col='id')

    non_uploaded = df.loc[df['updated']==False]

    for index, row in df.iterrows():
        row['updated'] = True
    
    df.to_csv('memes_data.csv')

    # for index, row in non_uploaded.iterrows():
    #     print(row['url'])

    return non_uploaded
    

upload_files(give_un_uploaded_memes())