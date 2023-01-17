from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# try:
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     name_inp =  browser.find_element(By.NAME, "firstname").send_keys('Max')
#     last_inp = browser.find_element(By.NAME, "lastname").send_keys('Smirnov')
#     mail_inp = browser.find_element(By.NAME, "email").send_keys('email@yo.com')
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, 'file.txt')
#     send = browser.find_element(By.ID, 'file').send_keys(file_path)
#     button = browser.find_element(By.CLASS_NAME, "btn-primary")
#     button.click()
# finally:
#     time.sleep(10)
#     browser.quit()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.CLASS_NAME, "btn-primary")
#     button.click()
#     alert = browser.switch_to.alert
#     alert.accept()
#     input_value = browser.find_element(By.ID, 'input_value').text
#     y = calc(input_value)
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#     button1 = browser.find_element(By.CLASS_NAME, "btn-primary")
#     button1.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

# try:
#         link = "http://suninjuly.github.io/redirect_accept.html"
#         browser = webdriver.Chrome()
#         browser.get(link)
#         button = browser.find_element(By.CLASS_NAME, "trollface")
#         button.click()
#         new_window = browser.window_handles[1]
#         browser.switch_to.window(new_window)
#         input_value = browser.find_element(By.ID, 'input_value').text
#         y = calc(input_value)
#         input1 = browser.find_element(By.ID, "answer")
#         input1.send_keys(y)
#         button1 = browser.find_element(By.CLASS_NAME, "btn-primary")
#         button1.click()
#
# finally:
#         time.sleep(10)
#         browser.quit()

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/cats.html")
# browser.implicitly_wait(5)
#
#
# but = browser.find_element(By.ID, "button")

try:
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        price_text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        but = browser.find_element(By.CLASS_NAME, "btn-primary")
        but.click()
        input_value = browser.find_element(By.ID, 'input_value').text
        y = calc(input_value)
        input1 = browser.find_element(By.ID, "answer")
        input1.send_keys(y)
        button1 = browser.find_element(By.ID, "solve")
        button1.click()
finally:
        time.sleep(10)
        browser.quit()

