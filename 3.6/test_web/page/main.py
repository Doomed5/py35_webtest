from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from test_web.page.search import Search
from selenium import webdriver


class Main:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 30)
        self.vars = {}
        self.driver.get('https://ceshiren.com/')

    def search(self, keyword):
        self.driver.find_element(By.CSS_SELECTOR, '#search-button').click()
        input_element = self.driver.find_element(By.CSS_SELECTOR, '#search-term')
        input_element.send_keys(keyword)
        input_element.send_keys(Keys.ENTER)
        return Search
