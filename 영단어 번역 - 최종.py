from selenium import webdriver
import time
import csv

# 자동화된 크롬 창 실행
driver = webdriver.Chrome('./chromedriver')

# 파파고 웹 페이지 접속
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)

# 시간적 여유 3초
time.sleep(3)

# 작성할 'my_papago.csv' 파일을 생성하여 변수 'f'에 저장
f = open('./my_papago.csv', 'w', newline = '')

# CSV 파일을 작성하는 객체 변수 'wtr' 생성
wtr = csv.writer(f)

# 열 제목 작성
wtr.writerow(['영단어', '번역결과'])


print("<영어→한국어> csv 파일 작성")

# 무한 루프
while True:
    keyword = input('번역할 영단어 입력 (0 입력하면 종료) : ')
    if keyword == '0':
        print('번역 종료')
        break

    # 영단어 입력, 번역 버튼 클릭
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

	# 번역 결과 저장
    output = driver.find_element_by_css_selector('div#txtTarget').text
    
	# my_papago.csv 파일에 [영단어, 번역결과] 작성
    wtr.writerow([keyword, output])
    
	# 영단어 입력 칸 초기화
    driver.find_element_by_css_selector('textarea#txtSource').clear()

# 크롬 창 닫기
driver.close()

# 파일 닫기
f.close()




driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

# 영어 ↔ 한국어 버튼 한 번 클릭
driver.find_element_by_css_selector('button.btn_switch___x4Tcl').click()

f = open('./my_papago.csv', 'r',newline = '')
rdr = csv.reader(f)
next(rdr)

my_dict = {}

i=0
for row in rdr:
    my_dict[i]=row[1]
    i+=1
    
f.close()


print("<한국어→영어> 검색 결과")


j=0
for j in range(i):
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(my_dict[j])
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text

    print(my_dict[j], ":", output)

    driver.find_element_by_css_selector('textarea#txtSource').clear()
    
driver.close()
