from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://litecart.stqa.ru/en/'

    def click(self, *locator):
        """
        Clicks on WebElement
        :param locator: search strategy for find_element of a Web Element, ex. (By.ID, 'id')
        """
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_page(self, url: str=''):
        #logger.info(f'Opening page {self.base_url + url}')
        self.driver.get(self.base_url + url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def wait_for_element_to_disappear(self, *locator, error_message=''):
        self.wait.until(EC.invisibility_of_element_located(locator),
                   f'Element by locator: {locator} did not disappear and is present.\n{error_message}')

    def wait_for_element_to_be_visible(self, *locator, error_message=''):
        self.wait.until(EC.visibility_of_element_located(locator),
                   f'Element by locator: {locator} is not visible.\n{error_message}')

    def len_counting(self, expected_value, *locator):
        items = self.driver.find_elements(*locator)
        print(items)
        assert int(expected_value) == len(items), f'Expected {int(expected_value)}, but got {len(items)} items total.'

    def string_is_empthy(self, emthy_string, *locator):
        actual_string = self.driver.find_element(*locator).text
        assert int(len(actual_string)) == 0, f'Expected text {emthy_string}, but got {actual_string}'
