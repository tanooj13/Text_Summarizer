from bs4 import BeautifulSoup
import os
import pandas as pd
d = {'title':[]}

for file in os.listdir('data'):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc,'html.parser')
        # print(soup.prettify())

        t = soup.find('h2')
        title = t.get_text()
        d['title'].append(title)
    except Exception as e:
        print(e)

print(d)
df = pd.DataFrame(data=d)
df.to_csv('data.csv')

    