# 学习时间：2022/7/9 15:21
# 学习人：ZPB
import allure
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@allure.feature('编辑页面')
class Test_denglu():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.70.234/')
        self.driver.maximize_window()
        sleep(5)

    def teardown_class(self):
        self.driver.quit()

    @allure.story('登陆失败')
    def test_01(self):
        excepted = '登录失败，请检查您的用户名或密码是否填写正确。'
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="account"]').send_keys('zhangpengbo')
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys('zhang')
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        sleep(2)

        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        assert alert.text == excepted
        alert.accept()

        sleep(3)

    @allure.story('登陆成功')
    def test_02(self):
        excepted='我的地盘 - 禅道'
        self.driver.find_element(By.XPATH, '//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').clear()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys('zhangpengbo')
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        sleep(3)
        WebDriverWait(self.driver, 5).until(EC.title_is(excepted))
        sleep(2)
        assert self.driver.title == excepted
        sleep(3)

if __name__ == '__main__':
    pytest.main(['123.py'])
