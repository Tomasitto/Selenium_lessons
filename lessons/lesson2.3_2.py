from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button1 = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value")
    x = x.text

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))

    attention = browser.switch_to.alert
    print(attention.text)

    button_final =  browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button_final.click()
    
finally:
    time.sleep(10)
    browser.quit()