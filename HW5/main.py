import requests
from bs4 import BeautifulSoup

url = 'https://emojipedia.org/search/'
categories = ["nature", "music", "science"]

for category in categories:
    params = {'q': category}
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find('ol', class_='search-results')
    items = elements.find_all('a')
    i=0
    for item in items:
       print(item.text)
       i += 1
    print(f'В категории {category} {i} эмоджи.')
    print()