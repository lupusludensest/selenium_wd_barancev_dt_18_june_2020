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