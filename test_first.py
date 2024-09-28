
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestFirst():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_first(self):
    self.open_home_page()
    self.login(username = "admin", password = "secret")
    self.open_group_page()
    self.create_group(name="new", header="qweqwe", footer="qweqweqweqwe")
    self.return_to_group_page()
    self.logout()

  def logout(self):
    # разлогиниваемся
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def return_to_group_page(self):
    # возвращаемся на страницу групп
    self.driver.find_element(By.LINK_TEXT, "group page").click()

  def create_group(self, name, header, footer):
    # создаём новую группу
    self.driver.find_element(By.NAME, "new").click()
    # заполняем поля формы создания группы
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys(name)
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys(header)
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys(footer)
    # отправка данных для создания группы
    self.driver.find_element(By.NAME, "submit").click()

  def open_group_page(self):
    # переходим на вкладку группы
    self.driver.find_element(By.LINK_TEXT, "groups").click()

  def login(self, username, password):
    # логинимся
    self.driver.find_element(By.NAME, "user").click()
    self.driver.find_element(By.NAME, "user").send_keys(username)
    self.driver.find_element(By.NAME, "pass").send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def open_home_page(self):
    # открывается главная страница
    self.driver.get("http://localhost/addressbook/")
  
