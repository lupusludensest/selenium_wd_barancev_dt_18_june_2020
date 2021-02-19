# [x] Задание 17. Проверьте отсутствие сообщений в логе браузера
# Сделайте сценарий, который проверяет, не появляются ли в логе браузера сообщения при открытии страниц в учебном приложении, а именно -- страниц товаров в каталоге в административной панели.
#
# Сценарий должен состоять из следующих частей:
#
# 1) зайти rgb админку
# 2) открыть каталог, категорию, которая содержит товары (страница http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1)
# 3) последовательно открывать страницы товаров и проверять, не появляются ли в логе браузера сообщения (любого уровня)
#
# Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.
#
# -----
#
# Уложите созданный файл, содержащий сценарий, в ранее созданный репозиторий. В качестве ответа на задание отправьте ссылку на свой репозиторий и указание, какой именно файл содержит нужный сценарий.
#
# Submission status
# Attempt number	This is attempt 1.
# Submission status	Submitted for grading
# Grading status	Graded
# Last modified	Saturday, 25 July 2020, 7:19 PM
# Online text
# View summary
# Good evening, boss.
#
# Find here hw#17: https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/hw_17_dt_25_july_2020_1.py
# Repeatedly asking you: BC I am not writting the code "from the head" at the moment but refactoring what I got-recommend me, please, one of your courses on Python. I am pretty much sure you see ьу through.
#
# Sincerely, Vic
#
# Make changes to your submission
# Feedback
# Grade	сдано!
# Graded on	Sunday, 26 July 2020, 9:44 AM
# Graded by	Picture of Алексей БаранцевАлексей Баранцев
# Feedback comments
# Верно. Вы можете присмотреться к курсу https://software-testing.ru/edu/1-schedule/233-python-for-testers

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()
    wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
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
    print(f'\nWD capabilities: {wd.capabilities}\n')
    request.addfinalizer(wd.quit)
    return wd

def present_error(drw):
    drw.execute_script("setTimeout(function() { throw \"Pizdets\"; }, 1000);")
    time.sleep(1)

    # Log in as admin
def test_litecart(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "login").click()

    # Log in to catalog
    wait = WebDriverWait(driver, 15)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    links = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, ".//*[@id='content']/form/table/tbody/tr/td[./img and ./a]/a")))
    # "//form[@name='catalog_form']//a[./../..//input[contains(@name,'product')] and not(./i)]"

    for i in range(0, len(links)):
        links[i].click()
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#tab-general")))
        #present_error(driver) https://www.geeksforgeeks.org/get_log-driver-method-selenium-python/
        browser_log = driver.get_log("browser")
        for l in browser_log:
            print(f'Log in browser log: {l}')
        if (len(browser_log)):
            assert(False),'something in the browser log'
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        links = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, ".//*[@id='content']/form/table/tbody/tr/td[./img and ./a]/a")))
        # "//form[@name='catalog_form']//a[./../..//input[contains(@name,'product')] and not(./i)]"

    print(f'\nThere are {len(links)} links')
    print(f'There are {len(browser_log)} strings in the log {str(browser_log)}')

    time.sleep(2)