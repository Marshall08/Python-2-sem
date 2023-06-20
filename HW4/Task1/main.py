# https://codeshare.io/X8J44o

import requests
from bs4 import BeautifulSoup

pages = 1
while True:
    url = f'https://quotes.toscrape.com/page/{pages}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    button_next = soup.find('li', class_="next")
    if button_next != None:
        pages += 1
    else:
        break
print(pages)