from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Search:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def search_by(self, author=None, keyword=None):
        if author is not None:
            self.driver.find_element(By.NAME, 'user-selector-renamed').send_keys(author)
            self.driver.find_element(By.CSS_SELECTOR, 'li .selected').click()
        if keyword is not None:
            search_input = self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
            search_input.clear()
            search_input.send_keys(keyword)
            search_input.send_keys(Keys.ENTER)

        return self

    def get_results(self):
        return [element.text for element in self.driver.find_elements(By.CSS_SELECTOR, 'div.fps_topic')]

    def get_authors(self):
        return [element.get_attribute('data-user-card') for element in
                self.driver.find_elements(By.CSS_SELECTOR, 'div.fps_topic .author a')]
