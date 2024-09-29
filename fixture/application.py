from selenium import webdriver
from selenium.webdriver.common.by import By
from PythonForTester.fixture.session import SessionHelper
from PythonForTester.fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)



    def open_home_page(self):
        # открывается главная страница
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
