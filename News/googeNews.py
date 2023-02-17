from pygooglenews import GoogleNews
import pandas as pd

gn = GoogleNews()

def get_news(key, file):
    search = gn.search(key)
    df = pd.DataFrame(search['entries'])
    Array = pd.DataFrame([])
    Array['title'] = df['title']
    category = []
    for i in range(0, len(search['entries'])):
        category.append(key)
    Array['category'] = category
    _df = pd.DataFrame()
    df2 =Array['title'].str.split(pat=' - ', expand= True)
    df2[[0, 1]]
    _df['title'] = df2[0]
    _df['Journal'] = df2[1]
    _df['category'] = Array['category']
    _df.to_csv(file, index=False, encoding="utf-8")

get_news('psychology', 'psychology.csv')
get_news('business', 'business.csv')
get_news('history', 'history.csv')
get_news('politics', 'politics.csv')
get_news('finance', 'finance.csv')
get_news('literature', 'literature.csv')
get_news('gym', 'gym.csv')

csv_files = ["psychology.csv", "business.csv", "history.csv", "politics.csv", "finance.csv","literature.csv", "literature.csv" ]
df_append = pd.DataFrame()
#append all files together
for file in csv_files:
            df_temp = pd.read_csv(file)
            df_append = df_append.append(df_temp, ignore_index=True)

df_append.to_csv('dataset.csv', mode='a', index=False, encoding="utf-8", header=False)
