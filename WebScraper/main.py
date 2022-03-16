import pandas as pd
from bs4 import BeautifulSoup
import requests

f = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(f.text)

quotes = []
authors = []
tags = []

# print(soup.get_text())

for pages in range(1, 10):
    f = requests.get('https://quotes.toscrape.com/page/' + str(pages))
    soup = BeautifulSoup(f.text)

    for i in soup.findAll("div", {"class": "quote"}):
        quotes.append((i.find("span", {"class": "text"})).text)

    for j in soup.findAll("div", {"class": "quote"}):
        authors.append((j.find("small", {"class": "author"})).text)

    for k in soup.findAll("div", {"class": "tags"}):
        tags.append((k.find("meta"))['content'])

finaldf = pd.DataFrame(
    {'Quotes': quotes,
     'Authors': authors,
     'Tags': tags
     })

with open("file.txt", "w") as output:
    output.write(str(finaldf))
