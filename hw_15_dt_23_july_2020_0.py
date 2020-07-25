# [+] Задание 15. Постройте небольшой грид
# Установите виртуальную машину, внутри которой работает Windows, и создайте грид, который состоит из диспетчера, работающего на вашей основной машине, и двух узлов -- один тоже на основной машине, а другой внутри виртуальной машины.
#
# Настройте узлы так, чтобы в виртуальной машине был доступен браузер Internet Explorer, а на основной машине, наоборот, он был недоступен.
#
# Попробуйте запустить какие-нибудь тесты удалённо на этом гриде, указывая разные браузеры, и убедитесь, что Internet Explorer действительно запускается внутри виртуальной машины, а другие браузеры, наоборот, на вашей основной машине.
#
# Можно использовать любую систему виртуализации, но если у вас нет предпочтений -- берите https://www.virtualbox.org/
#
# Готовые образы Windows для разных систем виртуализации можно найти здесь: https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/
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

import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

@pytest.fixture
def driver(request):

    # 1) local grid:
    # 192.168.50.30:
    # java -jar selenium-server-standalone-2.53.1.jar -role hub
    # java -jar selenium-server-standalone-2.53.1.jar  -role node -browser browserName=chrome
    # 192.168.50.155:
    # java -jar selenium-server-standalone-2.53.1.jar  -role node -hub http://192.168.50.30:4444/wd/hub -browser "browserName=internet explorer"
    # see http://elementalselenium.com/tips/52-grid
    # I cannot use server 3.x, see https://github.com/SeleniumHQ/selenium/issues/3808

    wd = webdriver.Remote("http://192.168.50.30:4444/wd/hub",desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
    #wd = webdriver.Remote("http://192.168.50.30:4444/wd/hub",desired_capabilities=DesiredCapabilities.CHROME)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_local_grid(driver):
    driver.get("http://www.seleniumhq.org")
    time.sleep(5)