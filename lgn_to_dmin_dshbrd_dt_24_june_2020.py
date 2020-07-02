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
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#1.1 Click on Template
driver.find_element(By.XPATH, "//span[contains(text(), 'Template')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#1.2 Click on Logotype
driver.find_element(By.XPATH, "//span[contains(text(), 'Logotype')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#2 Click on Catalog
driver.find_element(By.XPATH, "//span[@class='fa-stack fa-lg icon-wrapper'][1]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#2.1 Click on Catalog
driver.find_element(By.XPATH, "//span[contains(text(), 'Catalog')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#2.2 Click on Product Groups
driver.find_element(By.XPATH, "//span[contains(text(), 'Product Groups')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#2.3 Click on Option Groups
driver.find_element(By.XPATH, "//span[contains(text(), 'Option Groups')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#2.4 Click on Manufacturers
driver.find_element(By.XPATH, "//span[contains(text(), 'Manufacturers')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#2.5 Click on Suppliers
driver.find_element(By.XPATH, "//span[contains(text(), 'Suppliers')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#2.6 Click on Delivery Statuses
driver.find_element(By.XPATH, "//span[contains(text(), 'Delivery Statuses')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#2.7 Click on Sold Out Statuses
driver.find_element(By.XPATH, "//span[contains(text(), 'Sold Out Statuses')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#2.8 Click on Quantity Units
driver.find_element(By.XPATH, "//span[contains(text(), 'Quantity Units')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#2.9 CSV Import/Export
driver.find_element(By.XPATH, "//span[contains(text(), 'CSV Import/Export')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#3 Click on Countries
driver.find_element(By.XPATH, "//span[contains(text(), 'Countries')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#4 Click on Currencies
driver.find_element(By.XPATH, "//span[contains(text(), 'Currencies')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#5 Click on Customers
driver.find_element(By.XPATH, "//i[@class='fa fa-user fa-stack-1x icon'][1]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#5.1 Click on Customers
driver.find_element(By.XPATH, "//span[contains(text(), 'Customers')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#5.2 Click on CSV Import/Export
driver.find_element(By.XPATH, "//span[contains(text(), 'CSV Import/Export')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#5.3 Click on CSV Newsletter
driver.find_element(By.XPATH, "//span[contains(text(), 'Newsletter')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#6 Click on Geo Zones
driver.find_element(By.XPATH, "//span[contains(text(), 'Geo Zones')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#7 Click on Languages
driver.find_element(By.XPATH, "//i[@class='fa fa-comments fa-stack-1x icon'][1]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#7.1 Click on Languages
driver.find_element(By.ID, "doc-languages").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#7.2 Click on Storage Encoding
driver.find_element(By.XPATH, "//span[contains(text(), 'Storage Encoding')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#8 Click on Modules
driver.find_element(By.XPATH, "//i[@class='fa fa-cube fa-stack-1x icon'][1]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#8.1 Click on Background Jobs
driver.find_element(By.XPATH, "//span[contains(text(), 'Background Jobs')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#8.2 Click on Customer
driver.find_element(By.ID, "doc-customer").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(3)

#8.3 Click on Shipping
driver.find_element(By.LINK_TEXT, "Shipping").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#8.4 Click on Payment
driver.find_element(By.XPATH, "//span[contains(text(), 'Payment')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#8.5 Click on Order Total
driver.find_element(By.XPATH, "//span[contains(text(), 'Order Total')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#8.6 Click on Order Success
driver.find_element(By.XPATH, "//span[contains(text(), 'Order Success')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#8.7 Click on Order Action
driver.find_element(By.XPATH, "//span[contains(text(), 'Order Action')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#9 Click on Orders
driver.find_element(By.XPATH, "//span[contains(text(), 'Orders')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)




driver.quit()




