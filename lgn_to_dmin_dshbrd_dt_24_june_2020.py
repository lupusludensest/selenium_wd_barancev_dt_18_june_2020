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
sleep(2)

# Verify if "Trying to access array offset on value of type null in" is on page
assert 'Trying to access array offset on value of type null in' in driver.find_element(By.XPATH, "//th[@colspan='4']").text
print('Text: ', driver.find_element(By.XPATH, "//th[@colspan='4']").text, ';')
driver.quit()



