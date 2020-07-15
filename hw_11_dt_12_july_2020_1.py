[x] Задание 11. Сделайте сценарий регистрации пользователя
# Сделайте сценарий для регистрации нового пользователя в учебном приложении litecart (не в админке, а в клиентской части магазина).
#
# Сценарий должен состоять из следующих частей:
#
# 1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты (чтобы не конфликтовало с ранее созданными пользователями, в том числе при предыдущих запусках того же самого сценария),
# 2) выход (logout), потому что после успешной регистрации автоматически происходит вход,
# 3) повторный вход в только что созданную учётную запись,
# 4) и ещё раз выход.
#
# В качестве страны выбирайте United States, штат произвольный. При этом формат индекса -- пять цифр.
#
# Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.
#
# Проверки можно никакие не делать, только действия -- заполнение полей, нажатия на кнопки и ссылки. Если сценарий дошёл до конца, то есть созданный пользователь смог выполнить вход и выход -- значит создание прошло успешно.
#
# В форме регистрации есть капча, её нужно отключить в админке учебного приложения на вкладке Settings -> Security.
#
# -----
#
# Уложите созданный файл, содержащий сценарий, в ранее созданный репозиторий. В качестве ответа на задание отправьте ссылку на свой репозиторий и указание, какой именно файл содержит нужный сценарий.
#
# Submission status
# Attempt number	This is attempt 2.
# Submission status	Submitted for grading
# Grading status	Graded
# Last modified	Monday, 13 July 2020, 8:48 PM
# Online text
# View summary
# Good evening, boss.
#
# Attempt #2 hw11:
#
# https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework11_dt_12_july_2020_0.py
#
# Truly yours, Vic
#
# ________
#
# Good evening, boss.
#
# Find herein hw11: https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework11_dt_12_july_2020_0.py
#
#  Sincerely, Vic
#
# Make changes to your submission
# Feedback
# Grade	сдано!
# Graded on	Tuesday, 14 July 2020, 8:09 AM
# Graded by	Picture of Алексей БаранцевАлексей Баранцев
# Feedback comments
# Исправлено.
#
# Previous attempts
# Attempt 1: Monday, 13 July 2020, 7:59 AM
# Submission status	Submitted for grading
# Online text
# View summary
# Good evening, boss.
#
# Find herein hw11: https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework11_dt_12_july_2020_0.py
#
#  Sincerely, Vic
#
# Feedback
# Grade	надо доработать
# Graded on	Monday, 13 July 2020, 8:22 AM
# Graded by	Picture of Алексей БаранцевАлексей Баранцев
# Feedback comments
# View summary
# Необходимо также учесть следующий пункт задания:
# 1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты
# (чтобы не конфликтовало с ранее созданными пользователями, в том числе при предыдущих запусках того же самого сценария).

import time
from random import randint
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver(request):
    # 1) Chrome:
    wd = webdriver.Chrome()

    # 2) Firefox:
    # wd = webdriver.Firefox()

    # 3) Edge:
    # wd = webdriver.Edge(executable_path="C:\Webdrivers\msedgedriver")

    # print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_campaigns(driver):
    wait = WebDriverWait(driver, 15)

    password = str(randint(1000, 9999))
    login = 'imiarek' + password
    print(login + ':' + password)

    # Go to registration form
    driver.get("http://localhost/litecart/")
    product = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#box-account-login tr")))[4]
    link = product.find_element(By.CSS_SELECTOR, "a")
    link.click()

    # Fill the form
    account_box = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#create-account.box")))[0]

    account_box.find_element(By.CSS_SELECTOR, "input[name=firstname]").send_keys(login)
    account_box.find_element(By.CSS_SELECTOR, "input[name=lastname]").send_keys(login)
    account_box.find_element(By.CSS_SELECTOR, "input[name=address1]").send_keys('Line1')
    account_box.find_element(By.CSS_SELECTOR, "input[name=postcode]").send_keys('12345')
    account_box.find_element(By.CSS_SELECTOR, "input[name=city]").send_keys('CityN')

    country_selector = account_box.find_element(By.CSS_SELECTOR, "#create-account.box select[name=country_code]")
    selector = Select(country_selector)
    selector.select_by_visible_text('United States')

    state_selector = account_box.find_element(By.CSS_SELECTOR, "#create-account.box select[name=zone_code]")
    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#create-account.box select[name=zone_code] option")))

    selector = Select(state_selector)
    selector.select_by_visible_text('Kansas')

    account_box.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys(login + '@example.com')
    account_box.find_element(By.CSS_SELECTOR, "input[name=phone]").send_keys(Keys.HOME + "5555555555")
    account_box.find_element(By.CSS_SELECTOR, "input[name=password]").send_keys(password)
    account_box.find_element(By.CSS_SELECTOR, "input[name=confirmed_password]").send_keys(password)
    account_box.find_element(By.CSS_SELECTOR, "button[name=create_account]").click()

    # 1st logout
    account_links = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navigation #box-account li a")))
    account_links[3].click()

    # Login
    login_form = \
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navigation form[name=login_form]")))[0]
    login_form.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys(login + '@example.com')
    login_form.find_element(By.CSS_SELECTOR, "input[name=password]").send_keys(password)
    login_form.find_element(By.CSS_SELECTOR, "button[name=login]").click()

    # 2d logout
    account_links = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navigation #box-account li a")))
    account_links[3].click()