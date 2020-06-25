import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(executable_path = "C:\Webdrivers\chromedriver")
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))