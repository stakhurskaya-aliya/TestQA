import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'http://saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = 'secret_sauce'

user_name = driver.find_element(By. XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")
password = driver.find_element(By. XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By. XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

#text_products = driver.find_element(By. XPATH, "//span[@class='title']")
#value_text_products = text_products.text
#print((value_text_products))
#assert value_text_products == "Products"
#print("Good")

#get_url = driver.current_url
#print(get_url)
#vassert url == get_url
#print("Good URL")
now_date = datetime.datetime.utcnow().strftime("%Y.%m")
driver.save_screenshot('screenshot.png')
time.sleep(30)
#driver.quit()