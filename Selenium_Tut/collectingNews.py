from bs4 import BeautifulSoup
import os
import pandas as pd

headlines = []


for file in os.listdir('newsData'):
    try:
        with open(f"newsData/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc,'html.parser')
        # print(soup.prettify())

        t = soup.find('h2')
        title = t.get_text()
        d['title'].append(title)
    except Exception as e:
        print(e)