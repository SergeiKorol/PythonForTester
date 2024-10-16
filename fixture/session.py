from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def logout(self):
        # разлогиниваемся
        self.app.driver.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def login(self, username, password):
        # логинимся
        self.app.open_home_page()
        self.app.driver.find_element(By.NAME, "user").click()
        self.app.driver.find_element(By.NAME, "user").send_keys(username)
        self.app.driver.find_element(By.NAME, "pass").send_keys(password)
        self.app.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def is_logged_in_as(self, username):
        return self.app.driver.find_element(By.XPATH, "//div/div[1]/form/b").text == "(" + username + ")"

    def is_logged_in(self):
        return len(self.app.driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.app.logout()
        self.login(username, password)
