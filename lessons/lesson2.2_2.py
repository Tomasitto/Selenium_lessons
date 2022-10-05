from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")

    x = browser.find_element(By.ID, "input_value")
    x = x.text
    a = browser.find_element(By.ID, "answer")
    a.send_keys(calc(x))
    print(x)

    option1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]') 
    option2 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]') 
    button = browser.find_element(By.XPATH, '/html/body/div/form/button')   
    browser.execute_script("return arguments[0].scrollIntoView(true);", a)

    option1.click()
    option2.click()
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()