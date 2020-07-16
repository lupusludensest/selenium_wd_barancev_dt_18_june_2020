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
# Submission status	No attempt
# Grading status	Not graded
# Last modified	-

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from random import randint
import os
import datetime

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

    # Log in to URL: http://localhost/litecart/en/
def test_litecart(driver):
    wait = WebDriverWait(driver, 15)
    # Click on three first items
    for x in range(0, 3):
        driver.get("http://localhost/litecart/")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.image"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "add_cart_product"))).click()
        driver.switchTo().alert().accept()
        # goods_in_cart = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cart-wrapper .quantity"))).text
        # print(f'Goods in the cart : {goods_in_cart}')

