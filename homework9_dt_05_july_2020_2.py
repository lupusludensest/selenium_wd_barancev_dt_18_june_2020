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
    print(f'WD capabilities: {wd.capabilities}\n')
    request.addfinalizer(wd.quit)
    return wd

# @pytest.mark.skipif(1 == 1, reason="pass the first test start the second at once" )
def test_countries(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.maximize_window()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    # String comparing:
    #   http://stackoverflow.com/questions/4806911/string-comparison-technique-used-by-python
    #   https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types
    #   https://www.programiz.com/python-programming/operators
    # Arrays
    #   http://www.i-programmer.info/programming/python/3942-arrays-in-python.html?start=1

    # 1) Check country and zones sorting for http://localhost/litecart/admin/?app=countries&doc=countries
    #   a) Iterate through rows and columns collecting country names and checking number of zones
    #   b) For countries with zones follow link, check table sorting there, navigate to original page

    # (a)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[name=countries_form] tr.row")))
    number_of_rows = len(rows)
    print(f'\nNumber of rows below: {number_of_rows};\n')
    country_names = [0 for i in range(number_of_rows)]
    for x in range(0, number_of_rows):
        row = rows[x]
        columns = row.find_elements(By.CSS_SELECTOR, "td")
        country = columns[4]
        zones = columns[5]

        # Check sorting for country names:
        country_names[x] = country.text
        print(f'{[x+1]}.Country name: {country_names[x]};\n')
        if (x > 0):
            assert country_names[x - 1] < country_names[x]

        # (b)
        number_of_zones = int(zones.text)
        print(f'Number of zones in {country_names[x]}: {number_of_zones};\n')
        if (number_of_zones > 0):
            country.find_element(By.CSS_SELECTOR, "a").click()
            zones_rows = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#table-zones tr:not(.header)")))
            # The last row is for adding new zone, it is not zone itself so len(zones_rows) - 1
            number_of_zones_rows = len(zones_rows) - 1
            zone_names = [0 for i in range(number_of_zones_rows)]
            for y in range(0, number_of_zones_rows):
                zones_row = zones_rows[y]
                zone_cell = zones_row.find_elements(By.CSS_SELECTOR, "td")[2]
                # Check sorting for zones names:
                zone_names[y] = zone_cell.text
                # zone_names[y] = zone_cell.find_element(By.CSS_SELECTOR , "input").get_attribute("value")
                print(f'Zone name: {zone_names[y]};\n')
                if (y > 0):
                    assert zone_names[y - 1] < zone_names[y]
            # Come back
            driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
            rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[name=countries_form] tr.row")))

# @pytest.mark.skipif(0 == 0, reason="pass the second test run the first only" )
def test_geo_zones(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.maximize_window()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    # 2) Check zones sorting for each country at the page http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[name=geo_zones_form] tr.row")))
    number_of_rows = len(rows)
    print(f'\nNumber of rows below: {number_of_rows};\n')
    country_names = [0 for i in range(number_of_rows)]
    for x in range(0, number_of_rows):
        row = rows[x]
        columns = row.find_elements(By.CSS_SELECTOR, "td")
        country = columns[2]
        print(f'{[x+1]}. Country: {country.text};\n')
        country.find_element(By.CSS_SELECTOR, "a").click()
        zones_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#table-zones tr:not(.header)")))
        number_of_zones_rows = len(zones_rows) - 1
        print(f'Number of zones: {number_of_zones_rows};\n')
        zone_names = [0 for i in range(number_of_zones_rows)]
        for y in range(0, number_of_zones_rows):
            zones_row = zones_rows[y]
            zone_cell = zones_row.find_elements(By.CSS_SELECTOR, "td")[2]
            zone_names[y] = zone_cell.find_element(By.CSS_SELECTOR, "option[selected=selected]").text
            print(f'Zone name: {zone_names[y]};\n')
            if (y > 0):
                assert zone_names[y - 1] < zone_names[y]
        # Come back
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
        rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[name=geo_zones_form] tr.row")))