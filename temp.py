import pandas as pd

df = pd.read_csv('memes_data.csv', index_col='id')

df.loc['dep6y7', 'updated'] = True

print(df.head())
temp = df.loc[df['updated']==False]

for index, row in temp.iterrows():
    print(row['url'])
df.to_csv('memes_data.csv')