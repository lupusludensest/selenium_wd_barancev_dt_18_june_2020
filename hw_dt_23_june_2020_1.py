# [+] Задание 4. Научитесь запускать разные браузеры
# Попробуйте запустить разработанный ранее сценарий логина во всех основных браузерах, доступных для вашей операционной системы.
#
# Windows -- запустите в Firefox (с использованием geckodriver), Chrome, Internet Explorer (или Edge).
#
# Linux -- запустите в Firefox (с использованием geckodriver) и Chrome.
#
# MacOS -- запустите в Firefox (с использованием geckodriver), Chrome, а при наличии Safari 10 также и в нём.
#
# Если всё получилось -- можете самостоятельно отметить задание как выполненное -- перейти на главную страницу курса и поставить галочку напротив этого задания.
#
# Если возникли затруднения -- задавайте вопросы в скайп-чат.
#
# Submission status
# Attempt number	This is attempt 1.
# Submission status	This assignment does not require you to submit anything online
# Grading status	Not graded
# Last modified	-
# __________________________________________________________________
# [+] Задание 6. Научитесь запускать Firefox Nightly
# Попробуйте запустить разработанный ранее сценарий логина в браузере Firefox Nightly (https://nightly.mozilla.org/). Если Selenium не может сам найти место, куда установлен Firefox Nightly -- укажите в параметрах запуска путь к браузеру.
#
# Если всё получилось -- можете самостоятельно отметить задание как выполненное -- перейти на главную страницу курса и поставить галочку напротив этого задания.
#
# Если возникли затруднения -- задавайте вопросы в скайп-чат.
#
# Submission status
# Attempt number	This is attempt 1.
# Submission status	This assignment does not require you to submit anything online
# Grading status	Not graded
# Last modified	-

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()
    # wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
    # wd = webdriver.Firefox()
    options = webdriver.FirefoxOptions()
    options.binary_location = "C:\\Program Files\\Firefox Nightly\\firefox.exe"
    options.add_argument("start-maximized")
    wd = webdriver.Firefox(firefox_options=options)
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

def test_example(driver):
    # pass
    driver.get("https://www.google.com/")
    driver.maximize_window()
    sleep(2)
    driver.find_element_by_name("q").clear()
    sleep(2)
    driver.find_element_by_name("q").send_keys("webdriver")
    sleep(2)
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Google Search"))
