import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from random import randint
import os

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

    # Log in to URL: http://localhost/litecart/admin/
def test_litecart(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.maximize_window()
    sleep(2)

    # Enter login: admin
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("admin")
    sleep(2)

    # Enter password: admin
    driver.find_element(By.NAME,"password").clear()
    driver.find_element(By.NAME,"password").send_keys("admin")
    sleep(2)

    # Click Login button
    driver.find_element(By.NAME,"login").click()
    sleep(2)

    # Click Catalog button
    driver.find_element(By.XPATH, "//span[contains(text(), 'Catalog')]").click()
    sleep(2)

    # Click Add New Product button
    add_product_btn = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.button")))
    add_product_btn[1].click()
    sleep(2)

    # Click on General folder
    driver.find_element(By.XPATH, "//a[contains(text(), 'General')]").click()
    sleep(2)

    # Fill out Name field
    driver.find_element(By.NAME, "name[en]").clear()
    driver.find_element(By.NAME,"name[en]").send_keys("Abirvalg")
    sleep(2)

    # Fill out Code field
    driver.find_element(By.NAME, "code").clear()
    driver.find_element(By.NAME,"code").send_keys("428958")
    sleep(2)

    # Check on Unisex checkbox
    driver.find_element(By.XPATH, "//input[@value='1-3']").click()
    sleep(2)

    # Fill out Quantity field
    driver.find_element(By.XPATH, "//input[@name='quantity']").clear()
    driver.find_element(By.XPATH,"//input[@name='quantity']").send_keys("4")
    sleep(2)

    # Fill out Quantity Unit field
    driver.find_element(By.NAME, "quantity_unit_id").click()
    sleep(2)

    # Fill out Delivery Status field
    driver.find_element(By.NAME, "delivery_status_id").click()
    sleep(2)

    # Fill out Sold Out Status field
    driver.find_element(By.NAME, "sold_out_status_id").click()
    sleep(2)

    # Upload a pic by clicking on Choose File button
    product_image = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'FB_IMG_1575747160887.png'))
    print(product_image)
    sleep(2)

    # Set data Date Valid From
    # driver.find_element(By.NAME, "date_valid_from").click()
    # sleep(2)
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "date_valid_from")))
    element.click()
    sleep(2)
    selector = Select(element)
    selector.select_by_visible_text('Today')
    print(f'\nElement: {element}; Selector: {selector}\n')






