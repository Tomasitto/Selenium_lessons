from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    a = browser.find_element(By.ID, "treasure")

    x = calc(a.get_attribute('valuex'))
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(x)


    option1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    option1.click() 

    option2 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    option2.click() 


    button = browser.find_element(By.XPATH,'/html/body/div/form/div/div/button')
    button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()