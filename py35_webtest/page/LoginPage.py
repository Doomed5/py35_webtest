
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator.userLocator import LoginLocator as loc


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, mobile, pwd):
        # 输入账号
        self.driver.find_element(*loc.mobile_loc).send_keys(mobile)
        # 输入密码
        self.driver.find_element(*loc.pwd_loc).send_keys(pwd)
        # 点击登录
        ele = self.driver.find_element(*loc.login_btn_loc)
        self.driver.execute_script("arguments[0].click()", ele)

    def get_page_error_info(self):
        # 获取页面错误信息
        res = self.driver.find_element(*loc.page_error_info_loc).text
        return res

    def get_pop_window_error_info(self):
        # 获取弹窗错误信息
        ele = WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(
            loc.pop_window_info_loc))
        res = ele.text
        return res
