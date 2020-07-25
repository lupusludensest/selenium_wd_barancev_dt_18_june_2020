# [+] Задание 16. Научитесь использовать облачный грид
# Запустить несколько тестов в каком-нибудь облачном сервисе на выбор:
#
# https://www.browserstack.com/
# https://www.gridlastic.com/
# https://saucelabs.com/
# https://testingbot.com/
#
# Если всё получилось -- можете самостоятельно отметить задание как выполненное -- перейти на главную страницу курса и поставить галочку напротив этого задания.
#
# Если возникли затруднения -- задавайте вопросы в скайп-чат.
#
# Submission status
# Attempt number	This is attempt 1.
# Submission status	This assignment does not require you to submit anything online
# Grading status	Not graded
# Last modified	-

from selenium.webdriver.common.by import By
from selenium import webdriver

url_login_password = 'https://viacheslavgurov1:FWXVz6D7Rq7kwy2D5UyE@hub-cloud.browserstack.com/wd/hub'

desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Firefox',
 'browser_version': '77.0',
 'os': 'Windows'
}

driver = webdriver.Remote(
    command_executor=url_login_password,
    desired_capabilities=desired_cap)
driver.get("https://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit()