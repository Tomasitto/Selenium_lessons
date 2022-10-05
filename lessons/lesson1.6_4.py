from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    a = browser.find_element(By.XPATH, "//*[@id='input_value']")

    x = calc(a.text)
    answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer.send_keys(x)


    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click() 

    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click() 


    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()