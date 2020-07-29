# [x] Задание 11. Сделайте сценарий регистрации пользователя
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

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from random import randint

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
    # wd = webdriver.Firefox()
    # options = webdriver.FirefoxOptions()
    # options.binary_location = "C:\\Program Files\\Firefox Nightly\\firefox.exe"
    # options.add_argument("start-maximized")
    # wd = webdriver.Firefox(firefox_options=options)
    # new method
    # wd = webdriver.Firefox()
    # new method more obviously
    # wd = webdriver.Firefox(capabilities={"marionette": True})
    # old method
    # wd = webdriver.Firefox(capabilities={"marionette": False})
    # wd = webdriver.Edge(executable_path="C:\Webdrivers\msedgedriver")
    # wd = webdriver.Ie()
    # wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    # wd = webdriver.Ie(capabilities={"IntroduceInstabilityByIgnoringProtectedModeSettings": True, "requireWindowFocus": True, "unexpectedAlertBehaviour": "dismiss", "ignoreZoomSetting": True})
    # print(f'\nCAPABILITIES: {wd.capabilities}\nEND CAPABILITIES')
    print(f'WD capabilities: {wd.capabilities}\n')
    request.addfinalizer(wd.quit)
    return wd

def test_litecart(driver):
    driver.get("http://localhost/litecart/en/")
    driver.maximize_window()

    # Generators of password and name
    password = str(randint(999, 9999))
    name = 'name' + password
    email = (name + '@sample.com')
    print(f'\nName: {name}, password: {password} and email: {email}')

    # Click on button New customers click here
    driver.find_element(By.XPATH, "//a[contains(text(),'New customers click here')]").click()
    sleep(2)

    # Locators
    TAX_ID = driver.find_element(By.NAME, "tax_id")
    COMPANY = driver.find_element(By.NAME, "company")
    FIRST_NAME = driver.find_element(By.NAME, "firstname")
    LAST_NAME = driver.find_element(By.NAME, "lastname")
    ADDRESS_1 = driver.find_element(By.NAME, "address1")
    ADDRESS_2 = driver.find_element(By.NAME, "address2")
    POST_CODE = driver.find_element(By.NAME, "postcode")
    CITY = driver.find_element(By.NAME, "city")
    COUNTRY_DROP_OUT = driver.find_element(By.XPATH, "//span[@class='selection']")
    EMAIL = driver.find_element(By.NAME, "email")
    PHONE = driver.find_element(By.NAME, "phone")
    PASSWORD = driver.find_element(By.NAME, "password")
    CONFIRMED_PASSWORD = driver.find_element(By.NAME, "confirmed_password")
    CREATE_ACCOUNT_BUTTON = driver.find_element(By.NAME, "create_account")

    # Input tax id: 987-76-5431 into the field Tax ID
    TAX_ID.clear()
    TAX_ID.send_keys('987-76-5431')

    # Input Company: Red Cucumber LLC into the field Company
    COMPANY.clear()
    COMPANY.send_keys('Red Cucumber LLC')

    # Input First Name: * into the field First Name
    FIRST_NAME.clear()
    FIRST_NAME.send_keys('First_' + name)

    # Input Last Name: * into the field Last Name
    LAST_NAME.clear()
    LAST_NAME.send_keys('Last_' + name)

    # Input Address 1: 2165 NW 184nd St into the field Address 1
    ADDRESS_1.clear()
    ADDRESS_1.send_keys('2165 NW 184nd St')

    # Input Address 2: No appartment Beach into the field Address 2
    ADDRESS_2.clear()
    ADDRESS_2.send_keys('No appartment')

    # Input Postcode: 33987 into the field Postcode
    POST_CODE.clear()
    POST_CODE.send_keys('33987')

    # Input City: North Miami into the field City
    CITY.clear()
    CITY.send_keys('North Miami')

    # Choose Country: United States into the field Country
    COUNTRY_DROP_OUT.click()
    driver.find_element(By.CSS_SELECTOR, "input.select2-search__field").clear()
    driver.find_element(By.CSS_SELECTOR, "input.select2-search__field").send_keys('United States')

    # Choose Zone/State/Province: Florida into the field Zone/State/Province
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#create-account.box select[name=zone_code]")))
    element.click()
    selector = Select(element)
    selector.select_by_visible_text('Florida')
    print(f'\nElement: {element}; Selector: {selector}\n')

    # Input Email: * into the field Email
    EMAIL.clear()
    EMAIL.send_keys(email)

    # Input Phone: 4074354433 into the field Phone
    PHONE.clear()
    PHONE.send_keys('4074354433')

    # Input Desired Password: * into the field Desired Password
    PASSWORD.clear()
    PASSWORD.send_keys(password)

    # Input Confirm Password: * into the field Confirm Password
    CONFIRMED_PASSWORD.clear()
    CONFIRMED_PASSWORD.send_keys(password)
    sleep(2)

    # Click Create Account button
    CREATE_ACCOUNT_BUTTON.click()
    sleep(2)

# В форме регистрации есть капча, её нужно отключить в админке учебного приложения на вкладке Settings -> Security.

    # Click Logout button 1th time
    account_links = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navigation #box-account li a")))
    account_links[3].click()

    # 1th time Login as registered user
    login_form = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navigation form[name=login_form]")))[0]
    login_form.find_element(By.NAME, "email").send_keys(name + '@sample.com')
    login_form.find_element(By.NAME, "password").send_keys(password)
    login_form.find_element(By.NAME, "login").click()

    # Click Logout button 2d time
    account_links = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navigation #box-account li a")))
    account_links[3].click()



