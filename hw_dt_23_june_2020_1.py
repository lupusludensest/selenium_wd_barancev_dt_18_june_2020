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
    # wd = webdriver.Edge(executable_path="C:\Webdrivers\msedgedriver")
    # wd = webdriver.Ie()
    # wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
    # print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    # pass
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys("webdriver")
    sleep(2)
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Google Search"))
