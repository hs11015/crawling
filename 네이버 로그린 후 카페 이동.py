from selenium import webdriver
import time

# 크롬창 생성
driver = webdriver.Chrome('./chromedriver')

login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(login_url)
time.sleep(3)

# 로그인
while (1) :
    my_id = input("id를 입력해주세요 : ")
    my_pw = input("pw를 입력해주세요 : ")
    a = input("제대로 입력하셨다면 0, 잘못 입력하셨다면 1을 입력해주세요 : ")

    if a==0:
        break

    
driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(2)

driver.find_element_by_id('log.login').click()
time.sleep(1)

# 코뮤니티로 이동
comu_url = 'https://cafe.naver.com/codeuniv'
driver.get(comu_url)
time.sleep(2)

# 게시판으로 이동
driver.find_element_by_id('menuLink90').click()
time.sleep(1)

# 프레임 전환
driver.switch_to.frame('cafe_main')
time.sleep(1)

# 첫 게시글으로 이동 및 내용 출력
driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(1)

content = driver.find_element_by_css_selector('div.se-component-content').text

count = 1

print('< {}번째 글 >'.format(count))
print(content + '\n')

# 반복으로 19개 추출
for i in range(19):
    count += 1

    driver.find_element_by_css_selector('a.BaseButton.btn_next.BaseButton--skinGray.size_default').click()
    time.sleep(1)

    content = driver.find_element_by_css_selector('div.se-component-content').text

    print('< {}번째 글 >'.format(count))
    print(content + '\n')

driver.close()
