import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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
sswopard = driver.find_element(By. XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By. XPATH, "//input[@id='login-button']")
button_login.click()

print("Click Login Button")

action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
action.move_to_element(red_t_shirt).perform()

time.sleep(5)
driver.save_screenshot('scrennshot_3.png')

#driver.execute_script("window.scrollTo(0, 500)")
action = ActionChains(driver)


time.sleep(5)

driver.save_screenshot('screenshot_2.png')

#text_products = driver.find_element(By. XPATH, "//span[@class='title']")
#value_text_products = text_products.text
#print((value_text_products))
#assert value_text_products == "Products"
#print("Good")

#get_url = driver.current_url
#print(get_url)
#vassert url == get_url
#print("Good URL")
#driver.save_screenshot('screenshot.png')
time.sleep(30)
#driver.quit()