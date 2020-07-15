[x]
# Задание 9. Проверить сортировку стран и геозон в админке Сделайте
# сценарии, которые проверяют сортировку стран и геозон(штатов)
# в учебном приложении litecart.
#
# 1) на странице http: // localhost / litecart / admin /?app = countries & doc = countries
# а) проверить, что страны расположены в алфавитном порядке б) для
# тех стран, у которых количество зон отлично от нуля - - открыть
# страницу этой страны и там проверить, что зоны расположены в
# алфавитном порядке
#
# 2) на странице http: // localhost / litecart / admin /?app = geo_zones & doc = geo_zones
# зайти в каждую из стран и проверить, что зоны расположены в алфавитном
# порядке
#
# Можно оформить сценарии либо как тесты, либо как отдельные исполняемые
# файлы.
#
#     Если возникают проблемы с выбором локаторов для поиска элементов
# - - обращайтесь в чат за помощью.
#
# - ----
#
# Уложите созданный файл, содержащий сценарий, в ранее созданный репозиторий.В
# качестве ответа на задание отправьте ссылку на свой репозиторий и
# указание, какой именно файл содержит нужный сценарий.
#     Submission
# status Attempt number
# This is attempt 1. Submission status Submitted
# for grading
# Grading status    Graded
# Last modified    Thursday, 9 July 2020, 7:52
# PM
# Online
# text
# View
# summary
# Добрый
# день, Алексей.
#
# https: // github.com / LupusLudensEst / SeleniumWD_Barancev_dt_18_june_2020 / blob / master / homework9_dt_05_july_2020_2.py
#
# П.С.Признаю, использовал уже написанный код, однако это МАКС на что я
# способен в настоящий момент.
#     С уважением, Вячеслав

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

rows=driver.find_elements(By.XPATH, ".//*[@id='table-zones']//tr [not(contains (@class, 'header'))]")
print ('Length of something: '+str(len(rows)) + '\n')
column_z = driver.find_elements(By.TAG_NAME, "td")

# Extracting data from coulumn #3(index 2)
zones_name = []
for elements in rows:
    column_z = elements.find_elements(By.TAG_NAME, "td")
    zones_name.append(column_z[2].text)
print(f'Column Z: {column_z[2].text}\n')
# It deletes and returns the last element from list with index i list.pop([i]), becuse it is the filter field
# by default deleted the last element
# Nothing to delete from empty list
# zones_name.pop()
sorted_zones_list = sorted(zones_name)
print(f'Zones name: {zones_name}\n')
print(f'Sorted zone names: {sorted_zones_list}\n')
assert zones_name == sorted_zones_list
print(f'Text of zones name: {str(zones_name.append(column_z[2].text))}\n')

# Get into everyone from the countries and verify that zones are in the alphabet order
driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
# Get into every from the countries
geozones_list_text = []
# Set of links for countries with the zones
geo_links = driver.find_elements_by_xpath(
    ".//*[@id='content']/form/table/tbody/tr[@class='row']/td [not(contains (@style,'text'))]/a")
for link in geo_links:
    print(f'Link get attribute: {link.get_attribute("href")}\n')
    geozones_list_text.append(link.get_attribute('href'))
print(f'Length geo links above: {len(geo_links)}\n')
# Append links into special array to prevent Selenium from
# errors like  this python Message: stale element reference: element is not attached to the page document

# Run through the lists in the opened pages
for i in range(len(geozones_list_text)):
    geozones_list = []  # Nullifying the list
    driver.get(geozones_list_text[i])
    geo_zones_in_selects = driver.find_elements_by_xpath(
        ".//*[@id='table-zones']/tbody/tr/td/select[starts-with(@name,'zones[') and not(contains (@aria-hidden,'true'))]/option[@selected='selected']")
    for geozones in geo_zones_in_selects:
        geozones_list.append(geozones.text)

    sorted_geozones_list = sorted(geozones_list)
    print(f'Geo zones list: {geozones_list}\n')
    assert geozones_list == sorted_geozones_list
print(f'Length geo zones in select: {len(geo_zones_in_selects)}\n')

driver.quit()
