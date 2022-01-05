import requests

samsung_url = 'https://finance.naver.com/item/main.nhn?code=005930'
raw = requests.get(samsung_url)
print(raw)
print(raw.text)
