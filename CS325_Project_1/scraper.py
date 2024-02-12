import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/future/article/20231130-climate-crisis-the-15c-global-warming-threshold-explained'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

#articles = soup.findAll('p', {'class': 'sc-eb7bd5f6-0 fYAfXe'})
articles = soup.findAll('section', {'class': 'sc-4e574cd-0'})
lines = []
'''links = []

for article in articles:

    hrefs = article.find_all('a', href=True)
    for href in hrefs:
        links.append(href['href'])
'''
for index, article in enumerate(articles):
    if index < len(articles)-4:
        lines.append(article.get_text())

#print(articles)
#print(articles[len(articles) - 2])
for line in lines:
    print(line)