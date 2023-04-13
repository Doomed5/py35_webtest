import pytest
from selenium import webdriver
from page.LoginPage import LoginPage
from page.indexPage import IndexPage

success_case_data = [
    {'mobile': 'wagyu2016@163.com', 'pwd': 'admin123456', 'excepted': '登录成功'}
]
error_case_data = [
    {'mobile': 'wagyu2016@163.com', 'pwd': '', 'excepted': '请输入密码'}
]
error_alert_data = [
{'mobile': 'wagyu2018@163.com','pwd':'admin123456','excepted':'用户不存在'},
{'mobile': 'wagyu2018@163.com','pwd':'12345','excepted':'密码有效长度是6到30个字符'},
{'mobile': 'wagyu2018@163.com','pwd':'0123456789012345678901234567891','excepted':'密码有效长度是6到30个字符'}
]


@pytest.fixture(scope='function')
def login_fixture():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.ketangpai.com/#/login')

    yield driver
    driver.quit()


class TestLogin:

    @pytest.mark.parametrize('case', success_case_data)
    def test_login_pass(self, case, login_fixture):
        driver = login_fixture
        login_page = LoginPage(driver)
        login_page.login(case['mobile'], case['pwd'])
        index_page = IndexPage(driver)
        res = index_page.is_login_success()
        assert res == case['excepted']

    @pytest.mark.parametrize('case', error_case_data)
    def test_login_mobile_error(self, case, login_fixture):
        driver = login_fixture
        login_page = LoginPage(driver)
        login_page.login(case['mobile'], case['pwd'])
        res = login_page.get_page_error_info()
        assert res == case['excepted']

    @pytest.mark.parametrize('case', error_alert_data)
    def test_login_fail_pop_window(self, case, login_fixture):
        driver = login_fixture
        login_page = LoginPage(driver)
        login_page.login(case['mobile'], case['pwd'])
        res = login_page.get_pop_window_error_info()
        assert res == case['excepted']
