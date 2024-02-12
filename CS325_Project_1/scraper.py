import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser

url = 'https://www.bbc.com/future/article/20231130-climate-crisis-the-15c-global-warming-threshold-explained'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

articles = soup.findAll('section', {'class': 'sc-4e574cd-0'})
lines = []

for index, article in enumerate(articles):
    if index < len(articles)-4:
        lines.append(article.get_text())


file = open("BBC Climate Crisis Summary.txt", "a")
for line in lines:
    file.write(line + "\n")
file.close()
