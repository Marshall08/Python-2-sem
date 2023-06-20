# https://codeshare.io/X8J44o

import requests
from bs4 import BeautifulSoup
i = 1
quotes = []

while True:
    url = f'https://quotes.toscrape.com/page/{i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='quote')

    for item in items:
        item_text = item.find('span', class_="text").text
        item_author = item.find('small', class_="author").text
        quotes.append(f'{item_text} - (c) {item_author}')
    button_next = soup.find('li', class_="next")
    if button_next != None:
        i += 1
    else:
        break

for m in enumerate(quotes):
    print(m)
