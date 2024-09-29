from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:
    def __init__ (self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)

    def logout(self):
        # разлогиниваемся
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_group_page(self):
        # возвращаемся на страницу групп
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        self.open_group_page()
        # создаём новую группу
        self.driver.find_element(By.NAME, "new").click()
        # заполняем поля формы создания группы
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # отправка данных для создания группы
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def open_group_page(self):
        # переходим на вкладку группы
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        # логинимся
        self.open_home_page()
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        # открывается главная страница
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()