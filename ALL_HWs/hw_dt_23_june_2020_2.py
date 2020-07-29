# [+] Задание 4. Научитесь запускать разные браузеры
# Попробуйте запустить разработанный ранее сценарий логина во всех основных браузерах, доступных для вашей операционной системы.
#
# Windows -- запустите в Firefox (с использованием geckodriver), Chrome, Internet Explorer (или Edge).
#
# Linux -- запустите в Firefox (с использованием geckodriver) и Chrome.
#
# MacOS -- запустите в Firefox (с использованием geckodriver), Chrome, а при наличии Safari 10 также и в нём.
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
# __________________________________________________________________
# [+] Задание 6. Научитесь запускать Firefox Nightly
# Попробуйте запустить разработанный ранее сценарий логина в браузере Firefox Nightly (https://nightly.mozilla.org/). Если Selenium не может сам найти место, куда установлен Firefox Nightly -- укажите в параметрах запуска путь к браузеру.
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

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

sleep(2)

#Input into search field "webdriver"
search = driver.find_element(By.NAME, "q")
search.clear()
search.send_keys('webdriver')
sleep(1)

#Click on "Google Search" button
driver.find_element(By.NAME, 'btnK').click()
sleep(2)

# Verify if "WebDriver - World Wide Web Consortium" is on the page
assert 'WebDriver - World Wide Web Consortium' in driver.find_element(By.XPATH, "//a[@href='https://www.w3.org/TR/webdriver/']").text
print('Text: ', (driver.find_element(By.XPATH, "//a[@href='https://www.w3.org/TR/webdriver/']").text)[:37], ';')

driver.quit()





