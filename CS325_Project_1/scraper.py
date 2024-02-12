import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Scrape data from a given article from the BBC news agency.')
parser.add_argument('-a', '--article_URL', type=str, default="https://www.bbc.com/future/article/20231130-climate-crisis-the-15c-global-warming-threshold-explained", help="The URL of the article you'd like summarized.")
#url = 'https://www.bbc.com/future/article/20231130-climate-crisis-the-15c-global-warming-threshold-explained'
#url = 'https://www.bbc.com/future/article/20240206-craftivism-the-introverts-guide-to-gentle-protest-for-climate'
#url = 'https://www.bbc.com/future/article/20240131-how-planting-trees-is-bringing-clean-water-to-a-tropical-nation'
#url = 'https://www.bbc.com/news/uk-england-essex-68274304'
#url = 'https://www.bbc.com/news/uk-england-lincolnshire-68272816'
args = parser.parse_args()
url = args.article_URL
page = requests.get(url)
'''start = int()
end = int()'''
print(url)
soup = BeautifulSoup(page.content, 'lxml')

articles = soup.findAll('section', {'class': 'sc-4e574cd-0'})
lines = []

for index, article in enumerate(articles):
    if index < (len(articles)-4):             # The bottom four lines of a given article are a horizontal spacer and the author summary
        lines.append(article.get_text())

#file_name = "BBC Climate Crisis Summary.txt"
#file_name = "Gentle Protest Summary.txt"
#file_name = "Planting Trees Summary.txt"
#file_name = "Littering Summary.txt"
#file_name = "Solar Farm Summary.txt"
file_name = (url[(url.rfind('/') + 10):len(url)].replace('-', ' ').title() + " Summary.txt")
file = open(file_name, "w")

for line in lines:
    file.write(line + "\n")

file.close()
