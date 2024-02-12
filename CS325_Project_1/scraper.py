import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/future/article/20231130-climate-crisis-the-15c-global-warming-threshold-explained'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

articles = soup.findAll('p', {'class': 'sc-eb7bd5f6-0 fYAfXe'})
#articles = soup.findAll('section', {'class': 'sc-e11d1f0-0 eVThlc'})
'''links = []

for article in articles:

    hrefs = article.find_all('a', href=True)
    for href in hrefs:
        links.append(href['href'])
'''
for article in articles:
    print(article.get_text())

#print(soup.get_text())
print(articles)