# [x] Задание 13. Сделайте сценарий работы с корзиной
# Сделайте сценарий для добавления товаров в корзину и удаления товаров из корзины.
#
# 1) открыть главную страницу
# 2) открыть первый товар из списка
# 2) добавить его в корзину (при этом может случайно добавиться товар, который там уже есть, ничего страшного)
# 3) подождать, пока счётчик товаров в корзине обновится
# 4) вернуться на главную страницу, повторить предыдущие шаги ещё два раза, чтобы в общей сложности в корзине было 3 единицы товара
# 5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
# 6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица
#
# Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.
#
# -----
#
# Уложите созданный файл, содержащий сценарий, в ранее созданный репозиторий. В качестве ответа на задание отправьте ссылку на свой репозиторий и указание, какой именно файл содержит нужный сценарий.
#
# Submission status
# Attempt number	This is attempt 1.
# Submission status	Submitted for grading
# Grading status	Not graded
# Last modified	Thursday, 16 July 2020, 11:44 PM
# Online text
# View summary
# Hello, Alexey.
#
# Find here hw13: https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/hw_13_dt_15_july_2020_0.py
#
# Confess again that at the moment I am not producing the code "from the head"-as you mentioned before with Alexander in Skype, I just refactor and combine what I have on this subject.
#
# So, can I ask you advise me your course to rise my Python coding skills?
#
# Sincerely, Vic

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
    # wd = webdriver.Firefox()
    # options = webdriver.FirefoxOptions()
    # options.binary_location = "C:\\Program Files\\Firefox Nightly\\firefox.exe"
    # options.add_argument("start-maximized")
    # wd = webdriver.Firefox(firefox_options=options)
    # new method
    # wd = webdriver.Firefox()
    # new method more obviously
    # wd = webdriver.Firefox(capabilities={"marionette": True})
    # old method
    # wd = webdriver.Firefox(capabilities={"marionette": False})
    # wd = webdriver.Edge(executable_path="C:\Webdrivers\msedgedriver")
    # wd = webdriver.Ie()
    # wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    # wd = webdriver.Ie(capabilities={"IntroduceInstabilityByIgnoringProtectedModeSettings": True, "requireWindowFocus": True, "unexpectedAlertBehaviour": "dismiss", "ignoreZoomSetting": True})
    # print(f'\nCAPABILITIES: {wd.capabilities}\nEND CAPABILITIES')
    print(f'\nWD capabilities: {wd.capabilities}\n')
    request.addfinalizer(wd.quit)
    return wd

def test_cart(driver):
    wait = WebDriverWait(driver, 15)
    items_to_add = 3
    for item in range(items_to_add):
        # Go to the 1st product page
        driver.get("https://litecart.stqa.ru/en/") # http://localhost/litecart/
        driver.maximize_window()
        # Click on the first item in the list
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product")))[0].click()
        # Add the product to the cart
        box_product = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#box-product")))[0]
        # Verify the quantity of items in the cart counter
        cart_item_quantity_element = driver.find_element(By.CSS_SELECTOR,"#cart-wrapper .quantity")
        cart_item_quantity = int(cart_item_quantity_element.text)
        print(f'\nItem #: {cart_item_quantity + 1}; index: {cart_item_quantity_element.text}')
        # If item has a select option
        selectors = box_product.find_elements(By.CSS_SELECTOR, "select[name='options[Size]']")
        if (len(selectors) > 0):
            Select(selectors[0]).select_by_index(1)
        # Click on Add To Cart button
        box_product.find_element(By.CSS_SELECTOR,"button[name=add_cart_product]").click()
        # Waiting new quantity counter in the cart
        while int(cart_item_quantity_element.text) <= cart_item_quantity:
            time.sleep(1)
        print(f'Items in the cart: {int(cart_item_quantity_element.text)}\n')
    time.sleep(4)

    # Delete items from the cart
    driver.get("https://litecart.stqa.ru/en/checkout") # http://localhost/litecart/en/checkout
    time.sleep(2)
    for item in range(items_to_add):
        driver.find_element(By.NAME, 'remove_cart_item').click()
        time.sleep(2)
