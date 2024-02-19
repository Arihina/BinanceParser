from pprint import pprint

import bs4
import fake_useragent
import requests

ref = "https://www.binance.com/ru/markets/overview/"
header = {"user-agent": fake_useragent.UserAgent().random}

response = requests.get(ref, headers=header).text
soup = bs4.BeautifulSoup(response, 'lxml')

divs = soup.find_all('div', {"direction": "ltr"})

coins = {}

for div in divs:
    link_block = div.find_next('a', {"data-bn-type": "link"})
    name_block = link_block.find_next('div', {"class": "body3 line-clamp-1 truncate text-t-third css-vurnku"})

    link = link_block.get('href')
    name = name_block.text

    coins[name] = "https://www.binance.com" + link

pprint(coins)
