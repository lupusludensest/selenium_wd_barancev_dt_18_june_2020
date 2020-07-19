# [x] Задание 14. Проверьте, что ссылки открываются в новом окне
# Сделайте сценарий, который проверяет, что ссылки на странице редактирования страны открываются в новом окне.
#
# Сценарий должен состоять из следующих частей:
#
# 1) зайти в админку
# 2) открыть пункт меню Countries (или страницу http://localhost/litecart/admin/?app=countries&doc=countries)
# 3) открыть на редактирование какую-нибудь страну или начать создание новой
# 4) возле некоторых полей есть ссылки с иконкой в виде квадратика со стрелкой -- они ведут на внешние страницы и открываются в новом окне, именно это и нужно проверить.
#
# Конечно, можно просто убедиться в том, что у ссылки есть атрибут target="_blank". Но в этом упражнении требуется именно кликнуть по ссылке, чтобы она открылась в новом окне, потом переключиться в новое окно, закрыть его, вернуться обратно, и повторить эти действия для всех таких ссылок.
#
# Не забудьте, что новое окно открывается не мгновенно, поэтому требуется ожидание открытия окна.
#
# Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.
#
# -----
#
# Уложите созданный файл, содержащий сценарий, в ранее созданный репозиторий.
# В качестве ответа на задание отправьте ссылку на свой репозиторий и указание,
# какой именно файл содержит нужный сценарий.

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

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
    print(f'\nWD capabilities: {wd.capabilities}\n')
    request.addfinalizer(wd.quit)
    return wd

# Claim a class like here: https://stackoverflow.com/questions/19377437/python-selenium-webdriver-writing-my-own-expected-condition
class window_other_than(object):
    def __init__(self, old_windows):
        self.old_windows = old_windows

    def __call__(self, driver):
        new_windows = driver.window_handles
        news = [i for i in new_windows if i not in self.old_windows]
        if len(news) > 0:
            return news[0]
        else:
            return False

# Go to main page: http://localhost/litecart/admin/
def test_countries(driver):
    driver.get('http://localhost/litecart/admin/')
    driver.maximize_window()
    time.sleep(1)

# Input into the field "Username"
    search = driver.find_element(By.NAME, "username")
    search.clear()
    search.send_keys('admin')
    time.sleep(1)

# Input into the field "Password"
    search = driver.find_element(By.NAME, "password")
    search.clear()
    search.send_keys('admin')
    time.sleep(1)

# Click on button "Login"
    driver.find_element(By.NAME, 'login').click()
    time.sleep(1)

# Go to the Add New Country page
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(.,'Add New Country')]")))[0].click()

# List of external URLs
    new_window_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#content form a[target=_blank]")))

# Define Selenium name for current window and for previous windows
    main_window = driver.current_window_handle
    previous_windows = driver.window_handles

# Iterate through the list of external URLs
    for x in range(len(new_window_links)):
        new_window_links[x].click()
        new_window = wait.until(window_other_than(previous_windows))
        driver.switch_to_window(new_window)
        print(f'External page title: {driver.title}')
        driver.close()
        driver.switch_to_window(main_window)

    time.sleep(2)