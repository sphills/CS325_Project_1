import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/future/article/20231130-climate-crisis-the-15c-global-warming-threshold-explained'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

articles = soup.findAll('section', {'class': 'sc-4e574cd-0'})
'''links = []

for article in articles:

    hrefs = article.find_all('a', href=True)
    for href in hrefs:
        links.append(href['href'])
'''
print(soup.get_text())
