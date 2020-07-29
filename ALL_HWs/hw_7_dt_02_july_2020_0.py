# [x] Задание 7. Сделайте сценарий, проходящий по всем разделам админки
# Сделайте сценарий, который выполняет следующие действия в учебном приложении litecart.
#
# 1) входит в панель администратора http://localhost/litecart/admin
# 2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
# 3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
#
# Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.
#
# Если возникают проблемы с выбором локаторов для поиска элементов -- обращайтесь в чат за помощью.
#
# -----
#
# Уложите созданный файл, содержащий сценарий, в ранее созданный репозиторий. В качестве ответа на задание отправьте ссылку на свой репозиторий и указание, какой именно файл содержит нужный сценарий.
#
# Submission status
# Attempt number	This is attempt 4.
# Submission status	Submitted for grading
# Grading status	Graded
# Last modified	Saturday, 4 July 2020, 10:51 PM
# Online text
# View summary
# Hello, boss.
#
# One more attempt. Hope last one.
#
# https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework_dt_02_july_2020_2.py
#
# Sincerely, Vic

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
print('Text is here: ', (driver.find_element(By.ID, "content").text)[:8], ';')

#1 Click on Appearance
driver.find_element(By.CSS_SELECTOR, 'span.name').click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)

#1.1 Click on Template
driver.find_element(By.XPATH, "//span[contains(text(), 'Template')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Template' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('1 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#1.2 Click on Logotype
driver.find_element(By.XPATH, "//span[contains(text(), 'Logotype')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Logotype' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('1.2 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#2 Click on Catalog
driver.find_element(By.XPATH, "//span[@class='fa-stack fa-lg icon-wrapper'][1]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Catalog' in driver.find_element(By.XPATH, "//span[contains(text(), 'Catalog')]").text
print('2 Word is here: ', (driver.find_element(By.XPATH, "//span[contains(text(), 'Catalog')]").text)[:30], ';')
sleep(2)

#2.1 Click on Catalog
driver.find_element(By.XPATH, "//span[contains(text(), 'Catalog')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Catalog' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('2.1 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#2.2 Click on Product Groups
driver.find_element(By.XPATH, "//span[contains(text(), 'Product Groups')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Product Groups' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('2.2 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#2.3 Click on Option Groups
driver.find_element(By.XPATH, "//span[contains(text(), 'Option Groups')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Option Groups' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('2.3 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#2.4 Click on Manufacturers
driver.find_element(By.XPATH, "//span[contains(text(), 'Manufacturers')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Manufacturers' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('2.4 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#2.5 Click on Suppliers
driver.find_element(By.XPATH, "//span[contains(text(), 'Suppliers')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Suppliers' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('2.5 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#2.6 Click on Delivery Statuses
driver.find_element(By.XPATH, "//span[contains(text(), 'Delivery Statuses')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Delivery Statuses' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('2.6 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#2.7 Click on Sold Out Statuses
driver.find_element(By.XPATH, "//span[contains(text(), 'Sold Out Statuses')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Sold Out Statuses' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('2.7 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#2.8 Click on Quantity Units
driver.find_element(By.XPATH, "//span[contains(text(), 'Quantity Units')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Quantity Units' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('2.8 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#2.9 Click on CSV Import/Export
driver.find_element(By.XPATH, "//span[contains(text(), 'CSV Import/Export')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'CSV Import/Export' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('2.9 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#3 Click on Countries
driver.find_element(By.XPATH, "//span[contains(text(), 'Countries')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Countries' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('3 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#4 Click on Currencies
driver.find_element(By.XPATH, "//span[contains(text(), 'Currencies')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Currencies' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('4 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#5 Click on Customers
driver.find_element(By.XPATH, "//i[@class='fa fa-user fa-stack-1x icon'][1]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Customers' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('5 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#5.1 Click on Customers
driver.find_element(By.XPATH, "//span[contains(text(), 'Customers')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Customers' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('5.1 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#5.2 Click on CSV Import/Export
driver.find_element(By.XPATH, "//span[contains(text(), 'CSV Import/Export')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'CSV Import/Export' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('5.2 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#5.3 Click on Newsletter
driver.find_element(By.XPATH, "//span[contains(text(), 'Newsletter')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Newsletter' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('5.3 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#6 Click on Geo Zones
driver.find_element(By.XPATH, "//span[contains(text(), 'Geo Zones')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Geo Zones' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('6 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#7 Click on Languages
driver.find_element(By.XPATH, "//i[@class='fa fa-comments fa-stack-1x icon'][1]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Languages' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('7 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#7.1 Click on Languages
driver.find_element(By.ID, "doc-languages").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Languages' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('7.1 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#7.2 Click on Storage Encoding
driver.find_element(By.XPATH, "//span[contains(text(), 'Storage Encoding')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Storage Encoding' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('7.2 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#8 Click on Modules
driver.find_element(By.XPATH, "//i[@class='fa fa-cube fa-stack-1x icon'][1]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Modules' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('8 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#8.1 Click on Background Jobs
driver.find_element(By.XPATH, "//span[contains(text(), 'Background Jobs')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Job Modules' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('8.1 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#8.2 Click on Customer
driver.find_element(By.ID, "doc-customer").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(3)
assert 'Customer' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('8.2 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#8.3 Click on Shipping
driver.find_element(By.LINK_TEXT, "Shipping").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Shipping' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('8.3 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#8.4 Click on Payment
driver.find_element(By.XPATH, "//span[contains(text(), 'Payment')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Payment' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('8.4 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#8.5 Click on Order Total
driver.find_element(By.XPATH, "//span[contains(text(), 'Order Total')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Order Total' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('8.5 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#8.6 Click on Order Success
driver.find_element(By.XPATH, "//span[contains(text(), 'Order Success')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Order Success Modules' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('8.6 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#8.7 Click on Order Action
driver.find_element(By.XPATH, "//span[contains(text(), 'Order Action')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Order Action' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('8.7 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#9 Click on Orders
driver.find_element(By.XPATH, "//i[@class='fa fa-shopping-cart fa-stack-1x icon'][1]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Orders' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('9 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#9.1 Click on Orders
driver.find_element(By.XPATH, "//span[contains(text(), 'Orders')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Orders' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('9.1 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#9.2 Click on Order Statuses
driver.find_element(By.XPATH, "//span[contains(text(), 'Order Statuses')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Order Statuses' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('9.2 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#10 Click on Pages
driver.find_element(By.XPATH, "//span[contains(text(), 'Pages')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Pages' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('10 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#11 Click on Reports
driver.find_element(By.XPATH, "//span[contains(text(), 'Reports')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Monthly Sales' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('11 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#11.1 Click on Monthly Sales
driver.find_element(By.XPATH, "//span[contains(text(), 'Monthly Sales')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Monthly Sales' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('11.1 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#11.2 Click on Most Sold Products
driver.find_element(By.XPATH, "//span[contains(text(), 'Most Sold Products')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Most Sold Products' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('11.2 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#11.3 Click on Most Shopping Customers
driver.find_element(By.XPATH, "//span[contains(text(), 'Most Shopping Customers')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Most Shopping Customers' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('11.3 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#12 Click on Settings
driver.find_element(By.XPATH, "//span[contains(text(), 'Settings')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Settings' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('12 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#12.1 Click on Store Info
driver.find_element(By.XPATH, "//span[contains(text(), 'Store Info')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Settings' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('12.1 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#12.2 Click on Defaults
driver.find_element(By.XPATH, "//span[contains(text(), 'Defaults')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Settings' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('12.2 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#12.3 Click on General
driver.find_element(By.XPATH, "//span[contains(text(), 'General')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Settings' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('12.3  Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#12.4 Click on Listings
driver.find_element(By.XPATH, "//span[contains(text(), 'Listings')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Settings' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('12.4 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#12.5 Click on Images
driver.find_element(By.XPATH, "//span[contains(text(), 'Images')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Settings' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('12.5 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#12.6 Click on Checkout
driver.find_element(By.XPATH, "//span[contains(text(), 'Checkout')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Settings' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('12.6 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#12.7 Click on Advanced
driver.find_element(By.XPATH, "//span[contains(text(), 'Advanced')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Settings' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('12.7 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#12.8 Click on Security
driver.find_element(By.XPATH, "//span[contains(text(), 'Security')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Settings' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('12.8 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#13 Click on Slides
driver.find_element(By.XPATH, "//span[contains(text(), 'Slides')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Slides' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('13 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#14 Click on Tax
driver.find_element(By.XPATH, "//span[contains(text(), 'Tax')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Tax Classes' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('14 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#14.1 Click on Tax Classes
driver.find_element(By.XPATH, "//span[contains(text(), 'Tax Classes')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Tax Classes' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('14.1 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#14.2 Click on Tax Rates
driver.find_element(By.XPATH, "//span[contains(text(), 'Tax Rates')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Tax Rates' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('14.2 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#15 Click on Translations
driver.find_element(By.XPATH, "//span[contains(text(), 'Translations')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Search Translations' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('15 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#15.1 Click on Search Translations
driver.find_element(By.XPATH, "//span[contains(text(), 'Search Translations')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Search Translations' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('15.1 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#15.2 Click on Scan Files
driver.find_element(By.XPATH, "//span[contains(text(), 'Scan Files')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Scan Files' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('15.2 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#15.3 Click on CSV Import/Export
driver.find_element(By.XPATH, "//span[contains(text(), 'CSV Import/Export')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'CSV Import/Export' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('15.3 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#16 Click on Users
driver.find_element(By.XPATH, "//span[contains(text(), 'Users')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'Users' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('16 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

#17 Click on vQmods
driver.find_element(By.XPATH, "//span[contains(text(), 'vQmods')]").click()
# для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
sleep(2)
assert 'vQmods' in driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text
print('17 Word is here: ', (driver.find_element(By.XPATH, "//h1[@style='margin-top: 0px;']").text)[:30], ';')
sleep(2)

driver.quit()




