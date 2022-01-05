import requests
from bs4 import BeautifulSoup

count = 0
keyword = input("뉴스 검색 키워드 : ")

for page in range(1,3): #range는 몇 번째 페이지에 있는 기사 출력할 지 결정
    url = 'https://search.hankyung.com/apps.frm/search.news?query='+keyword+'&page=' + str(page)
    raw = requests.get(url)

    soup = BeautifulSoup(raw.text, 'html.parser')

    box = soup.find('ul', {'class' : 'article'})

    all_title = box.find_all('em', {'class' , 'tit'})

    all_time = box.find_all('span',{'clsss','date_time'})
    
    a = 0

    print('<'+str(page)+'페이지 뉴스 기사 제목>')
    for title in all_title:
        t = title.text
        count = count + 1
        print(count,'-',all_time[a].text,'-',t.strip())
        a=a+1
    print()
