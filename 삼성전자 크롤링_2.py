from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

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

j=0
for j in range(i):
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(my_dict[j])
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text

    print(my_dict[j], ":", output)

    driver.find_element_by_css_selector('textarea#txtSource').clear()
    
driver.close()