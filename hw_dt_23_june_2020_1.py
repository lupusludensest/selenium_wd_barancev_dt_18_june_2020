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
