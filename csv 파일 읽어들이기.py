from selenium import webdriver
import time



def get_papago_result(input_english):
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(input_english)       # 영단어 자동 입력

    driver.find_element_by_css_selector('button#btnTranslate').click()      # 번역 버튼 자동 클릭

    time.sleep(1)       # 시간적 여유 1초

    return driver.find_element_by_css_selector('div#txtTarget').text      # 번역 결과



my_dict = {}

driver = webdriver.Chrome('./chromedriver')     # 자동화된 크롬 창 실행

papago_url = 'https://papago.naver.com/'        # 파파고 웹 페이지 접속
driver.get(papago_url)
time.sleep(3)       # 시간적 여유 3초

for i in range(5):
    question = input('번역할 영단어 입력 : ')       # 번역하고 싶은 영단어 입력받기
    my_dict[question] = get_papago_result(question)       # 번역 결과 사전에 저장
    
print(my_dict)      # 번역 사전에서 출력

driver.close()      # 크롬 창 닫기

