from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://music.163.com/')

# driver.find_element_by_id('kw').send_keys('北京疫情')

# driver.find_element_by_id('su').click()
driver.maximize_window()
driver.find_element_by_xpath('//a[@class="link s-fc3"]').click()
sleep(2)
driver.find_element('link text', '选择其他登录模式').click()
driver.find_element('id', 'j-official-terms').click()
driver.find_element('link text', 'QQ登录').click()
sleep(2)
handles = driver.window_handles
driver.switch.to_window(handles[1])
#driver.close()
driver.switch.to_frame('ptlogin_iframe')
driver.find_element('id', 'switcher_plogin').click()
driver.find_element('xpath', '//*[@id="u"]').send_keys('530316028')
driver.find_element('xpath', '//*[@id="p"]').send_keys('0987syw!')
driver.find_element('xpath', '//*[@id="login_button"]').click()