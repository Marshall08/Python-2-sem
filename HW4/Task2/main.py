# https://codeshare.io/X8J44o

import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
params = {'page': 1}
products = []
while True:
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for i, item in enumerate(items):
        item_name = item.find('h4', class_='card-title').text.strip('\n')
        item_price = item.find('h5').text
        products.append(f'{item_price} {item_name}')

    last_button = soup.find_all('a', class_='page-link')[-1].text
    if last_button == 'Next':
        params['page'] += 1
    else:
        break

for i, elem in enumerate(products):
    print(f'{i + 1}. {elem}')
