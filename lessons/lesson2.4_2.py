
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.ID, "input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x)
    x = x.text

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))

    solve_button = browser.find_element(By.ID, 'solve')
    solve_button.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()