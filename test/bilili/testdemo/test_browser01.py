from selenium import webdriver
from time import sleep

driver =webdriver.Chrome()

driver.get('http://www.baidu.com')

tsxt = driver.find_element('id','kw').send_keys('长津湖')
sleep(2)
#driver.find_element('id','su').click()

