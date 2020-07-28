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
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    # options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # wd = webdriver.Chrome(chrome_options=options)
    wd = webdriver.Chrome(desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}})
    request.addfinalizer(wd.quit)
    return wd

def test_litecart(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "login").click()

    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    table_products = driver.find_element_by_css_selector('table.dataTable')
    rows_products = table_products.find_elements_by_xpath('//td/img/following-sibling::a')
    list_products = []
    for row_product in rows_products:
        list_products.append(row_product.get_attribute('href'))
    for i in list_products:
        driver.get(i)
    for entry in driver.get_log('browser'):
        print(f'\n{entry}')
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
