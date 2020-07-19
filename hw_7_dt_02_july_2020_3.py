# [x] Задание 7. Сделайте сценарий, проходящий по всем разделам админки
# Сделайте сценарий, который выполняет следующие действия в учебном приложении litecart.
#
# 1) входит в панель администратора http://localhost/litecart/admin
# 2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
# 3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
#
# Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.
#
# Если возникают проблемы с выбором локаторов для поиска элементов -- обращайтесь в чат за помощью.
#
# -----
#
# Уложите созданный файл, содержащий сценарий, в ранее созданный репозиторий. В качестве ответа на задание отправьте ссылку на свой репозиторий и указание, какой именно файл содержит нужный сценарий.
#
# Submission status
# Attempt number	This is attempt 4.
# Submission status	Submitted for grading
# Grading status	Graded
# Last modified	Saturday, 4 July 2020, 10:51 PM
# Online text
# View summary
# Hello, boss.
#
# One more attempt. Hope last one.
#
# https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework_dt_02_july_2020_2.py
#
# Sincerely, Vic

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from time import sleep

@pytest.fixture
def wd(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('http://localhost/litecart/admin/')
sleep(2)

#Input into the field "Username"
search = driver.find_element(By.NAME, "username")
search.clear()
search.send_keys('admin')
sleep(1)

#Input into the field "Password"
search = driver.find_element(By.NAME, "password")
search.clear()
search.send_keys('admin')
sleep(1)

#Click on button "Login"
driver.find_element(By.NAME, 'login').click()
sleep(4)

menu_number = len(driver.find_elements_by_css_selector("ul#box-apps-menu > li"))

while menu_number:
    menu_number -= 1
    menu_items = driver.find_elements_by_css_selector("ul#box-apps-menu > li")
    menu_items[menu_number].click()
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    submenu_number = len(driver.find_elements_by_css_selector(".docs>li>a"))
    while submenu_number:
        submenu_number -= 1
        submenu_items = driver.find_elements_by_css_selector(".docs>li>a")
        submenu_items[submenu_number].click()
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

driver.quit()
