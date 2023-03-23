import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDwei:

    def setup(self):
        url = 'http://www.baidu.com'
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_xpath(self):
        # self.driver.find_element(By.XPATH, "//*[contains(@id, 'kw')]").send_keys('selenium')
        # self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys('selenium')
        # self.driver.find_element(By.CSS_SELECTOR, "[id = 'kw']").send_keys('selenium')
        # self.driver.find_element(By.CSS_SELECTOR, ".s_ipt").send_keys('selenium')
        self.driver.find_element(By.CSS_SELECTOR, "span input[id='kw']").send_keys('selenium')
        time.sleep(3)
        self.driver.find_element(By.XPATH , '//*[@class="bg s_btn"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH , '//*[@class="s-tab-item s-tab-item_1CwH- s-tab-pic_p4Uej s-tab-pic"]').click()
