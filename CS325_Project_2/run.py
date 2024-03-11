import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Scrape data from a given article from the BBC news agency.')
parser.add_argument('-i', '--check_input_file', type=bool, default=True, help="Whether or not to parse the URLs listed in the input_articles.txt file.")
parser.add_argument('-a', '--article_URL', type=str, help="The URL of the article you'd like summarized.")

args = parser.parse_args()
check_input_file = args.check_input_file
url = args.article_URL

def scrape_url(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    articles = soup.findAll('section', {'class': 'sc-4e574cd-0'})
    lines = []

    for index, article in enumerate(articles):
        if index < (len(articles)-4):             # The bottom four lines of a given article are a horizontal spacer and the author summary
            lines.append(article.get_text())

    file_name = (url[(url.rfind('/') + 10):len(url)].replace('-', ' ').title() + " Summary.txt")
    file = open(file_name, "w")

    for line in lines:
        file.write(line.replace('\u200a', ' ') + "\n")

    print("Your article was successfully summarized and written to the file", "\"" + file_name + "\"", "in the current directory")

    file.close()

#if (check_input_file):
input_file = open("input_articles.txt", "r")
for line in input_file:
    scrape_url(line.strip())
'''
elif (check_input_file) and (url is not None):
    scrape_url(url)
'''