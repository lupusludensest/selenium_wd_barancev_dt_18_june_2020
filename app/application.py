from pages.main_page import MainPage
# from pages.cntct_frm_page import ContactFormPage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        # self.cntct_frm_page = ContactFormPage(self.driver)