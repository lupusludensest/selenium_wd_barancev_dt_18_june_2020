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
from selenium.webdriver.common.proxy import Proxy, ProxyType

@pytest.fixture
def driver(request):
    #wd = webdriver.Ie()
    #wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe", desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}})
    #wd = webdriver.Chrome()
    #wd = webdriver.Chrome(desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpsProxy": "127.0.0.1:8888"}})
    #wd = webdriver.Firefox()
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = "127.0.0.1:8888" # Will work with "localhost:8888"
    # prox.socks_proxy = "127.0.0.1:8888" # Does not work with this
    prox.ssl_proxy = "127.0.0.1:8888" # Will work with "localhost:8888"

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    wd = webdriver.Chrome(desired_capabilities=capabilities)
    request.addfinalizer(wd.quit)


    return wd

def test_proxy(driver):
    # driver.delete_all_cookies()
    driver.get("https://ya.ru")
    browser_log = driver.get_log("browser")
    for l in browser_log:
        print(f'\nBrowser log: {l}')
    if (len(browser_log) == 0):
        assert (True), 'something in the browser log'