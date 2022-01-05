from bs4 import BeautifulSoup
import requests

KOSPI_url = 'https://finance.naver.com/sise/'
raw = requests.get(KOSPI_url)

soup = BeautifulSoup(raw.text, 'html.parser')

box = soup.find('div', {'class' : 'rgt'})
numbers = box.find_all('li')

print('< 최근 인기 검색 종목>')
for number in numbers:
    print(number.text)
print(soup)
