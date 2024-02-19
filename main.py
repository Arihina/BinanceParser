import bs4
import fake_useragent
import requests

ref = "https://www.binance.com/ru/markets/overview/"
header = {"user-agent": fake_useragent.UserAgent().random}

response = requests.get(ref, headers=header).text
soup = bs4.BeautifulSoup(response, 'lxml')

coins = soup.find('div', {"id": "__APP"})
