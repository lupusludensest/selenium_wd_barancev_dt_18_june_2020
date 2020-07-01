from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

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

# Verify if "Warning" is on page
assert 'Warning:' in driver.find_element(By.ID, "content").text
print('Text: ', (driver.find_element(By.ID, "content").text)[:8], ';')

#1 Click on Appearance
driver.find_element(By.CSS_SELECTOR, 'span.name').click()

#1.1 Click on Template
driver.find_element(By.XPATH, "//span[contains(text(), 'Template')]").click()


driver.quit()




