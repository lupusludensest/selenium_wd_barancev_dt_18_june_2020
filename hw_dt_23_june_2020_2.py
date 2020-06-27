from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

sleep(2)

#Input into search field "webdriver"
search = driver.find_element(By.NAME, "q")
search.clear()
search.send_keys('webdriver')
sleep(1)

#Click on "Google Search" button
driver.find_element(By.NAME, 'btnK').click()
sleep(2)

# Verify if "WebDriver - World Wide Web Consortium" is on page
assert 'WebDriver - World Wide Web Consortium' in driver.find_element(By.XPATH, "//a[@href='https://www.w3.org/TR/webdriver/']").text
print('Text: ', (driver.find_element(By.XPATH, "//a[@href='https://www.w3.org/TR/webdriver/']").text)[:37], ';')
driver.quit()





