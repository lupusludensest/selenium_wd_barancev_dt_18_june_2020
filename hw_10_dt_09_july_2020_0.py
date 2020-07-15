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

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
    # # wd = webdriver.Firefox()
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
    print(f'WD capabilities: {wd.capabilities}\n')
    request.addfinalizer(wd.quit)
    return wd

def test_litecart(driver):
    driver.get("http://localhost/litecart/en/")
    driver.maximize_window()

# 1
    # Verify text "Yellow Duck" is here on the good on main page
    text_on_good_mp = driver.find_element(By.XPATH, "//div[contains(text(),'Yellow Duck')][1]").text
    print(f'\nText on the main page: {text_on_good_mp}')

    # Verify regular price is here on the good on main page
    reg_prc_on_good_mp = driver.find_element(By.XPATH, "//s[@class='regular-price'][1]").text
    print(f'Regular price on the main page: {reg_prc_on_good_mp}')

    # Verify discount price is here on the good on main page
    dsc_prc_on_good_mp = driver.find_element(By.XPATH, "//strong[@class='campaign-price'][1]").text
    print(f'Discount price on the main page: {dsc_prc_on_good_mp}')

    # Regular price on the main page: regular price font is grey, R=G=B
    color_font_rpmp = driver.find_element_by_xpath("//s[@class='regular-price'][1]").value_of_css_property("color")

    # Discount price on the main page: regular price font is red and bold, G=B=0
    color_font_dpmp = driver.find_element_by_xpath("//strong[@class='campaign-price'][1]").value_of_css_property("color")

    # Verify regular price text < discount price on the main page
    size_rpmp = driver.find_element_by_xpath("//s[@class='regular-price'][1]").value_of_css_property('font-size')
    size_dpmp =  driver.find_element_by_xpath("//strong[@class='campaign-price'][1]").value_of_css_property('font-size')
    assert size_rpmp < size_dpmp
    print(f'Regular price size on main page: {size_rpmp} VS Discount price size on main page: {size_dpmp}')

    # Verify text is strikethrough on the main page
    outer_html_rpmp = driver.find_element_by_xpath("//s[@class='regular-price'][1]").get_attribute("outerHTML")
    print(f'OuterHTML on the main page: {outer_html_rpmp}')
    assert outer_html_rpmp.index("</s>") != -1
    assert "</s>" in outer_html_rpmp

    # Verify red text is bold on the main page
    red_text_bold_on_mp = driver.find_element_by_xpath("//strong[@class='campaign-price'][1]").get_attribute("outerHTML")
    print(f'Red text is bold on the main page: {red_text_bold_on_mp}\n')
    assert red_text_bold_on_mp.index("</strong>") != -1
    assert "</strong>" in red_text_bold_on_mp

# 2
    # Go to good page and verify text "Yellow Duck" is here
    driver.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")
    text_on_good_gp = driver.find_element(By.CSS_SELECTOR, "h1.title").text
    print(f'      Text on the good page: {text_on_good_gp}')
    # Go to good page and verify regular price "$20" is here
    reg_prc_on_good_gp = driver.find_element(By.CSS_SELECTOR, "s.regular-price").text
    print(f'      Regular price on the good page: {reg_prc_on_good_gp}')

    # Go to good page and verify discount price is here
    dsc_prc_on_good_gp = driver.find_element(By.CSS_SELECTOR, "strong.campaign-price").text
    print(f'      Regular price on the good page: {dsc_prc_on_good_gp}')

    # Regular price on the good page: regular price font is grey, R=G=B
    color_font_rpgp = driver.find_element_by_css_selector("s.regular-price").value_of_css_property("color")

    # Discount price on the good page: regular price font is red and bold, G=B=0
    color_font_dpgp = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("color")

    # Verify regular price text < discount price on the good page
    size_rpgp = driver.find_element(By.CSS_SELECTOR, "s.regular-price").value_of_css_property('font-size')
    size_dpgp =  driver.find_element(By.CSS_SELECTOR, "strong.campaign-price").value_of_css_property('font-size')
    assert size_rpgp < size_dpgp
    print(f'      Regular price size on the good page: {size_rpgp} VS Discount price size on good page: {size_dpgp}')

    # Verify text is strikethrough on the good page
    outer_html_rpgp = driver.find_element_by_xpath("//s[@class='regular-price']").get_attribute("outerHTML")
    print(f'      OuterHTML on the good page: {outer_html_rpgp}')
    assert outer_html_rpgp.index("</s>") != -1
    assert "</s>" in outer_html_rpgp

    # Verify red text is bold on the good page
    red_text_bold_on_gp = driver.find_element_by_xpath("//strong[@class='campaign-price'][1]").get_attribute("outerHTML")
    print(f'      Red text is bold on the good page: {red_text_bold_on_gp}')
    assert red_text_bold_on_gp.index("</strong>") != -1
    assert "</strong>" in red_text_bold_on_gp

    # Asserts, texts and prices are the same on the main and on the good pages
    assert text_on_good_mp == text_on_good_gp
    assert reg_prc_on_good_mp == reg_prc_on_good_gp
    assert dsc_prc_on_good_mp == dsc_prc_on_good_gp

    # Transforming RGBa into array
    def get_rgba_array(rgba_string):
        # Simpler way?
        rgba_string = rgba_string.split('(')[1]
        rgba_string = rgba_string.split(')')[0]
        rgba_array = rgba_string.split(',')
        for x in range(0, len(rgba_array)):
            rgba_array[x] = int(rgba_array[x])
        return rgba_array

    # Asserts regular prices on the main and on the good pages are of grey font, R=G=B
    color_font_rpmp = get_rgba_array(color_font_rpmp)
    assert color_font_rpmp[0] == color_font_rpmp[1]
    assert color_font_rpmp[1] == color_font_rpmp[2]
    print(f'\nRGBa of regular price on main page: {color_font_rpmp}')

    color_font_rpgp = get_rgba_array(color_font_rpgp)
    assert color_font_rpgp[0] == color_font_rpgp[1]
    assert color_font_rpgp[1] == color_font_rpgp[2]
    print(f'RGBa of regular price on good page: {color_font_rpgp}')

    # Asserts discount prices on the main and on the good pages are of red bold font, G=B=0
    color_font_dpmp = get_rgba_array(color_font_dpmp)
    assert color_font_dpmp[0] != 0
    assert color_font_dpmp[1] == 0
    assert color_font_dpmp[1] == color_font_dpmp[2]
    print(f'RGBa of discount price on main page: {color_font_dpmp}')

    color_font_dpgp = get_rgba_array(color_font_dpgp)
    assert color_font_dpgp[0] != 0
    assert color_font_dpgp[1] == 0
    assert color_font_dpgp[1] == color_font_dpmp[2]
    print(f'RGBa of discount price on good page: {color_font_dpgp}')