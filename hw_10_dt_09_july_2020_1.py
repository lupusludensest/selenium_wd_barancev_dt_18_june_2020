# [x] Задание 10. Проверить, что открывается правильная страница товара
# Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара в учебном приложении litecart.
#
# Более точно, нужно открыть главную страницу, выбрать первый товар в блоке Campaigns и проверить следующее:
#
# а) на главной странице и на странице товара совпадает текст названия товара
# б) на главной странице и на странице товара совпадают цены (обычная и акционная)
# в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
# г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
# (цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
# д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
#
# Необходимо убедиться, что тесты работают в разных браузерах, желательно проверить во всех трёх ключевых браузерах (Chrome, Firefox, IE).
#
# Можно оформить сценарии либо как тесты, либо как отдельные исполняемые файлы.
#
# Если возникают проблемы с выбором локаторов для поиска элементов -- обращайтесь в чат за помощью.
#
# -----
#
# Уложите созданный файл, содержащий сценарий, в ранее созданный репозиторий. В качестве ответа на задание отправьте ссылку на свой репозиторий и указание, какой именно файл содержит нужный сценарий.
#
# Submission status
# Attempt number	This is attempt 2.
# Submission status	Submitted for grading
# Grading status	Graded
# Last modified	Saturday, 11 July 2020, 5:28 PM
# Online text
# View summary
# Good afternoon, Alexey.
#
# Find hw#10 attempt#2:
#
# https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework10_dt_09_july_2020_0.py
#
# Strings 57-58 and 94-95 are used with ".value_of_css_property('font-size')" and give output: Regular price size on main page: 14.4px VS Discount price size on main page: 18px,
# and assert is OK.
#
# Проверифаил зачеркнутый и жирный текст assertми на наличие закрывающих тегов s и strong.
#
#  P.S. В Вашем тексте, Алексей? "...Если проверять размер -- можно получить совершенно другой результат. Например, если один текст написан в две строчки, но мелким шрифтом, он может оказаться "больше" (по высоте), чем текст, написанный более крупным шрифтом, но в две строки(В ОДНУ СТРОКУ???-правильно понимать так?). ..."
#
# Truly yours, Vic
#
# ________
#
# Good evening, Alexey.
#
# Find hw10 herein: https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework10_dt_09_july_2020_0.py
#
# Пожалуйста, дайте образчик ассерта в строках 65 и 95-я не смог найти ничего, что сработало.
#
# С уважением, Вячеслав
#
# Make changes to your submission
# Feedback
# Grade	сдано!
# Graded on	Sunday, 12 July 2020, 3:17 AM
# Graded by	Picture of Алексей БаранцевАлексей Баранцев
# Feedback comments
# Теперь верно. Да, правильно понимать так.
#
# Previous attempts
# Attempt 1: Saturday, 11 July 2020, 12:10 AM
# Submission status	Submitted for grading
# Online text
# View summary
# Good evening, Alexey.
#
# Find hw10 herein: https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework10_dt_09_july_2020_0.py
#
# Пожалуйста, дайте образчик ассерта в строках 65 и 95-я не смог найти ничего, что сработало.
#
# С уважением, Вячелав
#
# Feedback
# Grade	надо доработать
# Graded on	Saturday, 11 July 2020, 2:06 AM
# Graded by	Picture of Алексей БаранцевАлексей Баранцев
# Feedback comments
# View summary
# 1) Метод size возвращает размер элемента, а не размер шрифта, а в задании требуется проверить именно шрифт. Если проверять размер -- можно получить совершенно другой результат. Например, если один текст написан в две строчки, но мелким шрифтом, он может оказаться "больше" (по высоте), чем текст, написанный более крупным шрифтом, но в две строки. Либо элемент имеет большие поля (сверху и/или снизу), в итоге размер (высота) элемента будет существенно больше, чем размер шрифта. Проверяйте свойство "font-size".
#
# 2) Для жирного и зачёркнутого текста проверяйте наличие элементов с данными тегами.

import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()
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
    wd = webdriver.Edge(executable_path="C:\Webdrivers\msedgedriver")
    # wd = webdriver.Ie()
    # wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    # wd = webdriver.Ie(capabilities={"IntroduceInstabilityByIgnoringProtectedModeSettings": True, "requireWindowFocus": True, "unexpectedAlertBehaviour": "dismiss", "ignoreZoomSetting": True})
    # print(f'\nCAPABILITIES: {wd.capabilities}\nEND CAPABILITIES')
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def get_rgba_array(rgba_string):
    # Simpler way?
    rgba_string = rgba_string.split('(')[1]
    rgba_string = rgba_string.split(')')[0]
    rgba_array = rgba_string.split(',')
    for x in range(0, len(rgba_array)):
        rgba_array[x] = int(rgba_array[x])
    return rgba_array

def style_check(old_price_element,new_price_element):
    # How to check stroke and bold styles in any browser? I cannot find text-decoration for stroke in FF.
    # So I use "s"-tag for stroke and "strong"-tag for bold checks

    # check grey:
    old_price_color = old_price_element.value_of_css_property("color")
    print(f'Old price color: {old_price_color}')
    old_price_color = get_rgba_array(old_price_color)
    assert old_price_color[0] == old_price_color[1]
    assert old_price_color[1] == old_price_color[2]

    # check red:
    new_price_color = new_price_element.value_of_css_property("color")
    print(f'New price color: {new_price_color}')
    new_price_color = get_rgba_array(new_price_color)
    assert new_price_color[0] != 0
    assert new_price_color[1] == 0
    assert new_price_color[2] == 0

    # compare size, namely the height
    old_price_size = old_price_element.size
    print(f'Old price size: {old_price_size}')
    new_price_size = new_price_element.size
    print(f'New price size: {new_price_size}')
    assert old_price_size['height'] < new_price_size['height']


def test_campaigns(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("http://localhost/litecart/")
    product = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#box-campaigns li")))[0]
    link = product.find_element(By.CSS_SELECTOR,"a.link")
    name_element = product.find_element(By.CSS_SELECTOR,".name")
    regular_price_element = product.find_element(By.CSS_SELECTOR,"s.regular-price")
    campaign_price_element = product.find_element(By.CSS_SELECTOR,"strong.campaign-price")

    name = name_element.text
    print(f'\nName on main page: {name}')
    regular_price = regular_price_element.text
    print(f'Regular price on main page: {regular_price}')
    campaign_price = campaign_price_element.text
    print(f'Campaign price on main page: {campaign_price}')

    style_check(regular_price_element,campaign_price_element)

    # Go to the product page:
    link.click()
    product = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#box-product")))[0]
    name_element = product.find_element(By.CSS_SELECTOR,"[itemprop=name]")
    regular_price_element = product.find_element(By.CSS_SELECTOR,"s.regular-price")
    campaign_price_element = product.find_element(By.CSS_SELECTOR,"strong.campaign-price")

    assert name == name_element.text
    print(f'Name on product page: {name}')
    assert regular_price == regular_price_element.text
    print(f'Regular price on product page: {regular_price}')
    assert campaign_price == campaign_price_element.text
    print(f'Campaign price on product page: {campaign_price}')

    style_check(regular_price_element,campaign_price_element)