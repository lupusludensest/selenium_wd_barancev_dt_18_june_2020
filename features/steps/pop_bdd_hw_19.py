from behave import *

@given("Loginpage")
def open_homepage(context):
    context.app.main_page.open_page()

