import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture
def wd(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

# Init driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the url
driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
sleep(2)

#Input into the field "Username"
search = driver.find_element(By.NAME, "username")
search.clear()
search.send_keys('admin')
sleep(1)

#Input into the field "Password"
search = driver.find_element(By.NAME, "password")
search.clear()
search.send_keys('admin')
sleep(1)

#Click on button "Login"
driver.find_element(By.NAME, 'login').click()
sleep(2)

# Countries table/ct
ct = driver.find_elements(By.CSS_SELECTOR, "tr.row")
len_ct = len(ct)
# txt_ct = driver.find_elements(By.CSS_SELECTOR, "tr.row").text
print(f'Lenght of table: {len_ct}')
# print(f'Text1: {txt_ct}\n')

# # Looking for column Name/cn
# cn = driver.find_elements(By.XPATH, "//*[@id='content']/form/table/tbody/tr[1]/th[5]")
# len_cn = len(cn)
# txt_cn = driver.find_element(By.XPATH, "//*[@id='content']/form/table/tbody/tr[1]/th[5]").text
# print(f'Lenght2: {len_cn}')
# print(f'Text2: {txt_cn}\n')
#
# # Looking for Zone/zn
# driver.get('http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=US')
# sleep(2)
# zn = driver.find_elements(By.XPATH, ".//*[@id='table-zones']//tr [not(contains (@class, 'header'))]")
# len_zn = len(cn)
# txt_zn = driver.find_element(By.XPATH, ".//*[@id='table-zones']//tr [not(contains (@class, 'header'))]").text
# print(f'Lenght3: {len_zn}')
# print(f'Text3: {txt_zn}\n')


driver.quit()
