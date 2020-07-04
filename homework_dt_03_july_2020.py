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

# Count and print how many goods are here on the page
stickers = 0 # see below: stickers = stickers + len(sticker)
goods_on_page = driver.find_elements(By.XPATH, ".//ul[@class='listing-wrapper products']//li")
total = len(goods_on_page)
print(f'Goods on the page: {total}')

# Verify every good has a sticker
for good in goods_on_page:
        sticker = good.find_elements(By.XPATH, ".//div[starts-with(@class,'sticker')]")
        stickers = stickers + len(sticker) # see above: stickers = 0
assert len(goods_on_page) == stickers

# Print out the length of the sticker ant total of stickers
print(f'Length of sticker: {len(sticker)}')
print(f'Stickers: {stickers}')

driver.quit()