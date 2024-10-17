from selenium import webdriver
from PythonForTester.fixture.session import SessionHelper
from PythonForTester.fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        # открывается главная страница
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
