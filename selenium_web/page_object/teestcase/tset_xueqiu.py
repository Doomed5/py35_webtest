import time

from selenium import webdriver

from page_object.page.MainPage import MainPage


class TestXuQiu(object):
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://xueqiu.com/')
        time.sleep(2)
        self.main = MainPage(self.driver)

    def test_search(self):
        self.main.search('alibaba').follow('1688')

    def teardown(self):
        pass
