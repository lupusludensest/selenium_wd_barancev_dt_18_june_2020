# [x] Задание 8. Сделайте сценарий, проверяющий наличие стикеров у товаров
# Сделайте сценарий, проверяющий наличие стикеров у всех товаров в учебном приложении litecart на главной странице. Стикеры -- это полоски в левом верхнем углу изображения товара, на которых написано New или Sale или что-нибудь другое. Сценарий должен проверять, что у каждого товара имеется ровно один стикер.
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
# Last modified	Tuesday, 7 July 2020, 8:09 PM
# Online text
# View summary
# Good evening, boss.
#
# See third attempt:
#
# https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework8_dt_03_july_2020.py
#
# Sincerely, Vic
#
#  _____________
#
# Good morning, boss.
#
# See second attempt: https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework8_dt_03_july_2020.py
#
# Truly yours, VIc
#
#  _____________
#
# Hello, boss.
#
# Have a nice weekend.
#
# https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework_dt_03_july_2020.py
#
# Sincerely, Vic
#
# Make changes to your submission
# Feedback
# Grade	сдано!
# Graded on	Wednesday, 8 July 2020, 6:41 AM
# Graded by	Picture of Алексей БаранцевАлексей Баранцев
# Feedback comments
# Fixed.
#
# Previous attempts
# Attempt 3: Monday, 6 July 2020, 8:51 PM
# Submission status	Submitted for grading
# Online text
# View full(53 words)
# Good morning, boss.
#
# See second attempt: https://github....
#
# Feedback
# Grade	надо доработать
# Graded on	Tuesday, 7 July 2020, 9:01 AM
# Graded by	Picture of Алексей БаранцевАлексей Баранцев
# Feedback comments
# View summary
# Не нашёл нужных исправлений в файле https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework8_dt_03_july_2020.py. Проверка выглядит сейчас так: assert len(goods_on_page) == stickers. То есть сравнивается общее количество товаров на странице и количество стикеров. Вместо этого необходимо проверить, что количество стикеров каждого товара равно единице.
#
# Attempt 2: Saturday, 4 July 2020, 10:53 PM
# Attempt 1: Friday, 3 July 2020, 11:37 PM

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('http://localhost/litecart/en/')
sleep(2)

# Count and print out how many goods are here on the page
stickers = 0 # see below: stickers = stickers + len(sticker)
goods_on_page = driver.find_elements(By.XPATH, ".//ul[@class='listing-wrapper products']//li")
total = str(len(goods_on_page))
print(f'Goods on the page: {total}\n')

# Verify every good has a sticker
for good in goods_on_page:
        sticker = good.find_elements(By.XPATH, ".//div[starts-with(@class,'sticker')]")
        print(f"Pic # {stickers+1} has {len(sticker)} sticker(s).")
        stickers = stickers + len(sticker) # see above: stickers = 0
assert len(goods_on_page) == stickers
assert len(sticker) == 1
print(f'\nThere are {len(goods_on_page)} goods on the page and {stickers} stickers.\n')

driver.quit()