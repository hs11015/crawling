from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)

time.sleep(3)
driver.close()
