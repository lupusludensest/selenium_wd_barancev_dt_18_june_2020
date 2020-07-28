# [+] Задание 18. Перенаправьте трафик в прокси-сервер
# Установите какой-нибудь прокси-сервер, который умеет протоколировать запросы и ответы.
#
# На выбор прокси-сервера для разных платформ:
# http://www.telerik.com/fiddler (Windows)
# https://www.charlesproxy.com/ (Windows, Linux, MacOS, платный, но есть пробная версия)
# https://mitmproxy.org/ (Linux, MacOS)
# https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project (Windows, LInux, MacOS)
#
# Инициализируйте драйвер так, чтобы запросы из браузера отправлялись через этот прокси-сервер, убедитесь, что они там видны.
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
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.proxy import Proxy, ProxyType

@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()
    # wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
    # wd = webdriver.Chrome(desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}})

    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = "127.0.0.1:8888"
    # prox.socks_proxy = "127.0.0.1:8888" # Does not work with this
    prox.ssl_proxy = "127.0.0.1:8888"

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    wd = webdriver.Chrome(desired_capabilities=capabilities)

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
            print(f'\nBrowser log: {l}')
        if (len(browser_log) != 0):
            assert(True),'something in the browser log'
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        links = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, ".//*[@id='content']/form/table/tbody/tr/td[./img and ./a]/a")))
        # "//form[@name='catalog_form']//a[./../..//input[contains(@name,'product')] and not(./i)]"

    print(f'\nThere are {len(links)} links')
    print(f'There are {len(browser_log)} strings in the log {str(browser_log)}')

    time.sleep(2)