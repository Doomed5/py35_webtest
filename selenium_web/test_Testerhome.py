from selenium import webdriver

class TestTesterHome():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://testerhome.com/')
    def test_mtsc2023(self):
        self.driver.find_element_by_link_text('MTSC 2023 上海站 + 深圳站议题征集').click()
        self.driver.find_element_by_xpath('//*[@data-toggle="dropdown"]').click()
