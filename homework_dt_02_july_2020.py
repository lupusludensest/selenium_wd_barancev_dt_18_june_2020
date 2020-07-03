from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('http://localhost/litecart/admin/')

sleep(2)

#Input into the field "Username"
search = driver.find_element(By.NAME, "username")
search.clear()
search.send_keys('admin')
sleep(1)

#Input into the field "Password"
search = driver.find_element(By.NAME, "password")
search.clear()
search.send_keys('admin')
sleep(1)

#Click on button "Login"
driver.find_element(By.NAME, 'login').click()
sleep(4)

#Click on all items in unordered list
list_1 = driver.find_elements(By.XPATH, "//li[@id='app-']")
# list_1 = driver.find_elements(By.CSS_SELECTOR, "span.name")
n=len(list_1)
for i in range(n):
    print(f"#{i+1}/{n}; Text: {list_1[i].text}; Element: {list_1[i]}")
    sleep(1)
    # (list_1[i]).click()
    sleep(2)

driver.quit()


# a = [43, 65, 54, 43, 6, 43]
# # обход по значениям
# # count = 0
# # for i in a:
# #     print(i, a.index(i))
#
# # обход по индексам
# n=len(a)
# for i in range(n):
#     print(i+1, a[i])
#     a[i]+=5
# print(a)
#
# a=[1,2,3,4,32,4,5,3,5]
# b=[]
# for i in a:
#     if not i in b:
#         b.append(i)
# print(b)
#
# even=[]
# odd=[]
# n=len(a)
# for i in range(n):
#     if a[i]%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even, odd)

# str= 'HeLLo WorlD'
# for i in str:
#     if 'a'<=i<='z':
#         print(i, 'small')
#     elif 'A'<=i<='Z':
#         print(i, 'big')
#     else:
#         print(i, 'is not letter')