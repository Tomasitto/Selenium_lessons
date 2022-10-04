from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    a = browser.find_element(By.ID, "num1")
    a = int(a.text)

    b = browser.find_element(By.ID, "num2")
    b = int(b.text)

    c = str(int(a) + int(b))
    print(c)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(c)
    
    

    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()