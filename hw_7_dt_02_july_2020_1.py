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

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Creation of Menu Items
menu_items = driver.find_elements(By.CSS_SELECTOR, "span.name")
names_items = []
for item in menu_items:
    if item in menu_items:
        names_items.append(item.text)

# Printing of Names of items and their quantity
print(f"{names_items}\n", end = ' ')
print(f"Total: {len(names_items)}")

# Clicking on all items presented and verifying each has an element with tag "h1"
for name_item in names_items:
    driver.find_element(By.XPATH, "//span[text()[contains(.,'" + name_item + "')]]").click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

driver.quit()
