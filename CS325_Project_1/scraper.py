import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser

#url = 'https://www.bbc.com/future/article/20231130-climate-crisis-the-15c-global-warming-threshold-explained'
url = 'https://www.bbc.com/future/article/20240206-craftivism-the-introverts-guide-to-gentle-protest-for-climate'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

articles = soup.findAll('section', {'class': 'sc-4e574cd-0'})
lines = []

for index, article in enumerate(articles):
    if index < (len(articles)-4):             # The bottom four lines of a given article are a horizontal spacer and the author summary
        lines.append(article.get_text())

#file_name = "BBC Climate Crisis Summary.txt"
file_name = "Gentle Protest Summary.txt"
file = open(file_name, "w")

for line in lines:
    file.write(line + "\n")

file.close()
