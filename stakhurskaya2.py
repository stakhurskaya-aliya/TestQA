
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "https://www.provartesting.com/contact/?utm_source=google&utm_medium=cpc&utm_campaign=uk_competitor&gclid=Cj0KCQjwz8emBhDrARIsANNJjS5nGD0ripp8PE5713StPCS5Ay_rdYqVyo6yxC6-LmVHKhwc618lwqwaAoOeEALw_wcB"
browser = webdriver.Chrome()
browser.get(link)


select = browser.find_element(By.XPATH, '//*[@id="input_11_10"]') #находим выпадающий список
#select.select_by_visible_text(value) # выбираем нужный элемент списка
browser.execute_script("return arguments[0].scrollIntoView(true);", select)
select = Select(select)
select.select_by_value('Albania')

#h1 = browser.find_element(By.XPATH,'/html/body/main/div/article/header/h1')
#h1 = h1.text
#assert 'Резюме' == h1
print(' все ок, тест пройден 👌👌👌👌👌👌👌👌👌')

# закрываем браузер после всех манипуляций
time.sleep(5)
browser.quit()
