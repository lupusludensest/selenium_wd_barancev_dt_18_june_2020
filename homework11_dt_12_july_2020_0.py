import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
    # # wd = webdriver.Firefox()
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

def test_litecart(driver):
    driver.get("http://localhost/litecart/en/")
    driver.maximize_window()

    # 1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты (чтобы не конфликтовало
    # с ранее созданными пользователями, в том числе при предыдущих запусках того же самого сценария),\
    # Click on button New customers click here
    driver.find_element(By.XPATH, "//a[contains(text(),'New customers click here')]").click()

    # Input tax id: 987-76-5431 into the field Tax ID
    driver.find_element(By.NAME, "tax_id")
    driver.find_element(By.NAME, "tax_id").clear()
    driver.find_element(By.NAME, "tax_id").send_keys('987-76-5431')

    # Input Company: Red Cucumber LLC into the field Company
    driver.find_element(By.NAME, "company")
    driver.find_element(By.NAME, "company").clear()
    driver.find_element(By.NAME, "company").send_keys('Red Cucumber LLC')

    # Input First Name: Holden into the field First Name
    driver.find_element(By.NAME, "firstname")
    driver.find_element(By.NAME, "firstname").clear()
    driver.find_element(By.NAME, "firstname").send_keys('Holden')

    # Input Last Name: Colfield into the field Last Name
    driver.find_element(By.NAME, "lastname")
    driver.find_element(By.NAME, "lastname").clear()
    driver.find_element(By.NAME, "lastname").send_keys('Colfield')

    # Input Address 1: 2165 NW 184nd St into the field Address 1
    driver.find_element(By.NAME, "address1")
    driver.find_element(By.NAME, "address1").clear()
    driver.find_element(By.NAME, "address1").send_keys('2165 NW 184nd St')

    # Input Address 2: No appartment Beach into the field Address 2
    driver.find_element(By.NAME, "address2")
    driver.find_element(By.NAME, "address2").clear()
    driver.find_element(By.NAME, "address2").send_keys('No appartment')

    # Input Postcode: 33987 into the field Postcode
    driver.find_element(By.NAME, "postcode")
    driver.find_element(By.NAME, "postcode").clear()
    driver.find_element(By.NAME, "postcode").send_keys('33987')

    # Input City: North Miami into the field City
    driver.find_element(By.NAME, "city")
    driver.find_element(By.NAME, "city").clear()
    driver.find_element(By.NAME, "city").send_keys('North Miami')

    # Choose Country: United States into the field Country
    driver.find_element(By.XPATH, "//span[@class='selection']").click()
    driver.find_element(By.CSS_SELECTOR, "input.select2-search__field")
    driver.find_element(By.CSS_SELECTOR, "input.select2-search__field").clear()
    driver.find_element(By.CSS_SELECTOR, "input.select2-search__field").send_keys('United States')

    # Choose Zone/State/Province: Florida into the field Zone/State/Province
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#create-account.box select[name=zone_code]")))
    element.click();
    selector = Select(element)
    selector.select_by_visible_text('Florida')
    print(f'\nElement: {element}; Selector: {selector}\n')

    # Input Email: sanoy2006@rambler.ru into the field Email
    driver.find_element(By.NAME, "email")
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys('4sanoy2006@rambler.ru')

    # Input Phone: 4074354433 into the field Phone
    driver.find_element(By.NAME, "phone")
    driver.find_element(By.NAME, "phone").clear()
    driver.find_element(By.NAME, "phone").send_keys('4074354433')

    # Input Desired Password: Test12!@ into the field Desired Password
    driver.find_element(By.NAME, "password")
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys('Test12!@')

    # Input Confirm Password: Test12!@ into the field Confirm Password
    driver.find_element(By.NAME, "confirmed_password")
    driver.find_element(By.NAME, "confirmed_password").clear()
    driver.find_element(By.NAME, "confirmed_password").send_keys('Test12!@')
    sleep(10)

    # Click Create Account button
    driver.find_element(By.NAME, "create_account").click()
    sleep(4)

# Did not find how to bypass Captcha - so I installed sleep(10) and during these 10 sec filled manually
# В форме регистрации есть капча, её нужно отключить в админке учебного приложения на вкладке Settings -> Security.

    # Click Logout button
    # driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
    # driver.find_element(By.XPATH, "//a[@href='http://localhost/litecart/en/logout']").click()
    account_links = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navigation #box-account li a")))
    account_links[4].click()

    # 1th Login as registered user
    driver.find_element(By.NAME, "email")
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys('4sanoy2006@rambler.ru')

    driver.find_element(By.NAME, "password")
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys('Test12!@')

    # Click in checkbox Remember Me remember_me
    driver.find_element(By.NAME, "remember_me").click()

    # Click on Login button
    driver.find_element(By.NAME, "login").click()
    sleep(4)

    # Click Logout button
    # driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
    account_links = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navigation #box-account li a")))
    account_links[3].click()


