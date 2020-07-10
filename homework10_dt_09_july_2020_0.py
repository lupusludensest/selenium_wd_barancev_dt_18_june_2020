import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
    assert 'Yellow Duck' == text_on_good_mp
    # Verify regular price "$20" is here on the good on main page
    reg_prc_on_good_mp = driver.find_element(By.XPATH, "//s[@class='regular-price'][1]").text
    print(f'\nRegular price on the main page: {reg_prc_on_good_mp}')
    assert '$20' == reg_prc_on_good_mp
    # Verify discount price "$18" is here on the good on main page
    dsc_prc_on_good_mp = driver.find_element(By.XPATH, "//strong[@class='campaign-price'][1]").text
    print(f'\nDiscount price on the main page: {dsc_prc_on_good_mp}')
    assert '$18' == dsc_prc_on_good_mp
# 2
    # Go to good page and verify text "Yellow Duck" is here
    driver.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")
    text_on_good_gp = driver.find_element(By.CSS_SELECTOR, "h1.title").text
    print(f'\nText on the good page: {text_on_good_gp}')
    assert 'Yellow Duck' == text_on_good_gp
    # Go to good page and verify regular price "$20" is here
    reg_prc_on_good_gp = driver.find_element(By.CSS_SELECTOR, "s.regular-price").text
    print(f'\nRegular price on the good page: {reg_prc_on_good_gp}')
    assert '$20' == reg_prc_on_good_gp
    # Go to good page and verify discount price "$18" is here
    dsc_prc_on_good_gp = driver.find_element(By.CSS_SELECTOR, "strong.campaign-price").text
    print(f'\nRegular price on the good page: {dsc_prc_on_good_gp}')
    assert '$18' == dsc_prc_on_good_gp
# 3
    # Verify regular price is crossed out and gray (we can assume that the “gray” color is one with
    # the same values in the RGBa representation for the R, G and B channels)
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
    assert old_price_color[0] == old_price_color[0]
    assert old_price_color[1] == old_price_color[2]

    # check red:
    new_price_color = new_price_element.value_of_css_property("color")
    print(f'New price color: {new_price_color}')
    new_price_color = get_rgba_array(new_price_color)
    assert new_price_color[0] > 0
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