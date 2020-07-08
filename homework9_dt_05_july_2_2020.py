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

# Creating lists:
cities_names = []
cities_with_names_zones =[]
country_zones = []
country_items = driver.find_elements(By.XPATH, "//tr[contains(@class,'row')]//a[not(@title='Edit')]")
for country_item in country_items:
    cities_names.append(country_item.text)

print(str(cities_names.append(country_item.text)))
print(len(country_items))

cities_names_sorted = sorted(cities_names)
assert cities_names_sorted == cities_names

country_item_text = country_item.find_element(By.XPATH, ".//../../td[6]").text
for country_item in country_items:
    country_cities_zones = int(country_item_text)
print(country_cities_zones, country_item_text)
if country_cities_zones > 0:
    cities_with_names_zones.append(country_item_text)
print(str(cities_with_names_zones))


driver.quit()