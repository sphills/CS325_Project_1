import requests
from bs4 import BeautifulSoup

url = 'https://www.reuters.com/markets/commodities/coal-india-beats-third-quarter-profit-estimates-higher-production-2024-02-12/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
articles = soup.findAll('div', {'class': 'list media_rows list-berita'})
links = []

for article in articles:

    hrefs = article.find_all('a', href=True)
    for href in hrefs:
        links.append(href['href'])

print(links)