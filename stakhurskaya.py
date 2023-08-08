
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://strizhechenko.github.io/2020/03/09/computers2020.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(10)
a1 = browser.find_element(By.XPATH, '/html/body/header/div/nav/div/a')
a1.click()
time.sleep(10)

h1 = browser.find_element(By.XPATH,'/html/body/main/div/article/header/h1')
h1 = h1.text
assert 'Резюме' == h1
print('😜😜😜😜😜😜😜Михаил!!!, все ок, тест пройден 👌👌👌👌👌👌👌👌👌')

# закрываем браузер после всех манипуляций
time.sleep(5)
browser.quit()
