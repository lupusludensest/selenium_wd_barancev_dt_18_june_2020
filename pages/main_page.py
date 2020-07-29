from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait

class MainPage(Page):

    # Add to cart
    def click_first_product(self, times):
        wait = WebDriverWait(self.driver, 10)
        for i in range(int(times)):
            # Click on first item in the list
            self.driver.find_elements(By.CSS_SELECTOR, ".product")[0].click()
            # In case item has a select option
            box_product = self.driver.find_elements(By.CSS_SELECTOR, "#box-product")[0]
            selectors = box_product.find_elements(By.CSS_SELECTOR, "select[name='options[Size]']")
            if (len(selectors) > 0):
                Select(selectors[0]).select_by_index(1)
            # Click on Add To Cart button
            self.driver.find_element(By.NAME, "add_cart_product").click()
            # Waiting new quantity counter in the cart
            counter = int(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.quantity"))).text)
            WebDriverWait(self.driver, 10).until(lambda s: int(s.find_element(By.CSS_SELECTOR, "span.quantity").text) == counter + 1)
            goods_in_cart = (counter + 1)
            print(f'\n        Items in the cart: {goods_in_cart}')
            # Step back in the browser hystory
            self.driver.back()

    # Delete from cart
    def del_from_cart(self):
        wait = WebDriverWait(self.driver, 10)
        # Click on checkout
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#cart a.link"))).click()
        # Iterate delete till table with items is not empthy
        counter = len(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.dataTable tr"))).text)
        while counter > 0:
            wait.until(EC.element_to_be_clickable((By.NAME, "remove_cart_item"))).click()
            WebDriverWait(self.driver, 10).until(
                lambda s: len(s.find_elements(By.CSS_SELECTOR, "table.dataTable tr")) < counter)
            counter = len(self.driver.find_elements(By.CSS_SELECTOR, "table.dataTable tr"))
            print(f'\nRows in the table after deleting one more item: {counter}')
            # Step back in the browser hystory
        self.driver.back()
