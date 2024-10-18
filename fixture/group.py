from selenium.webdriver.common.by import By
from PythonForTester.model.group import Group

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
        self.fill_group_form(group)
        # отправка данных для создания группы
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_name("group_name", group.name)
        self.change_field_name("group_header", group.header)
        self.change_field_name("group_footer", group.footer)

    def change_field_name(self, field_name, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).clear()
            self.app.driver.find_element(By.NAME, field_name).send_keys(text)

    def open_group_page(self):
        if self.app.driver.current_url.endswith("/group.php") and len(self.app.driver.find_elements(By.NAME, "new")) > 0:
            return
        # переходим на вкладку группы
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        # перейти на страницу с группами
        self.open_group_page()
        self.select_first_group()
        self.app.driver.find_element(By.NAME, "delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_first_group(self):
        self.app.driver.find_element(By.NAME, "selected[]").click()

    def modify_first_group(self, new_group_data):
        self.open_group_page()
        self.select_first_group()
        # open modification form
        self.app.driver.find_element(By.NAME, "edit").click()
        # fill
        self.fill_group_form(new_group_data)
        # submit modification
        self.app.driver.find_element(By.NAME, "update").click()
        # logout
        self.return_to_group_page()
        self.group_cache = None

    def count(self):
        self.open_group_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_groups_list(self):
        if self.group_cache is None:
            self.open_group_page()
            self.group_cache = []
            for element in self.app.driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id_element = element.find_elements(By.NAME, "selected[]")
                if id_element:  # Проверяем, что список не пуст
                    id = id_element[0].get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
