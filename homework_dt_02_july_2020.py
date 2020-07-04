from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('http://localhost/litecart/admin/')
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
sleep(4)

# Creation of Menu Items
menu_items = driver.find_elements(By.CSS_SELECTOR, "span.name")
names_items = []
for item in menu_items:
    if item in menu_items:
        names_items.append(item.text)

# Printing of Names of items and their quantity
print(f"{names_items}\n", end = ' ')
print(f"Total: {len(names_items)}")

# Clicking on all items presented and verify each has an element with tag "h1"
for name_item in names_items:
    driver.find_element(By.XPATH, "//span[text()[contains(.,'" + name_item + "')]]").click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

driver.quit()
