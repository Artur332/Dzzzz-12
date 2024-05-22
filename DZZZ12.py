import requests
from bs4 import BeautifulSoup

Site = 'http://books.toscrape.com'
response = requests.get(Site)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h3')

for title in titles:
    print(title.text.strip)
