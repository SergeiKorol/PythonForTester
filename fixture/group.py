from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        # возвращаемся на страницу групп
        self.app.driver.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
        self.open_group_page()
        # создаём новую группу
        self.app.driver.find_element(By.NAME, "new").click()
        # заполняем поля формы создания группы
        self.app.driver.find_element(By.NAME, "group_name").click()
        self.app.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.driver.find_element(By.NAME, "group_header").click()
        self.app.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.app.driver.find_element(By.NAME, "group_footer").click()
        self.app.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # отправка данных для создания группы
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def open_group_page(self):
        # переходим на вкладку группы
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()
