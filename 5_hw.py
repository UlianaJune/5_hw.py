ДЗ 5/1

if__name__=="__main__""
button = Button("КнопкиЭ")
input_field = Input("Поля")
title = Title("Заголовок")
link = Link("Ссылки")

    print(button.check_text())
    print(input_field.check_text())
    print(title.check_text())
    print(link.check_text())

from selenium import webdriver
from selenium.webdriver.common.by import By

def check_elements():

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username_field = driver.find_element(By.ID, "user.name")
password_field = driver.find_element(By.ID, "user.password")
submit_button = driver.find_element(By.ID, "logon.button")

if username_field and password_field and submint_button:
    print:("Элементы найдены")
else:
    print:("Элементы не найдены")
driver.quit()
check_elements()
