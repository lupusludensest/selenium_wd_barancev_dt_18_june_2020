from behave import *

@given("Loginpage")
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()

@then("Click on the first item from the list {times} times")
def click_first_product(context, times):
    """
    Click on the first item from the list
    """
    context.app.main_page.click_first_product(times)


@then("Click on checkout button and delete all items from the bin")
def del_from_cart(context):
    """
    Click on checkout button and delete all items from the bin
    """
    context.app.main_page.del_from_cart()