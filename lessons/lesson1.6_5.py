from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
    input1.send_keys('Tomas')

    input2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
    input2.send_keys('Mann')

    input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
    input3.send_keys('Gucci_gang@ya.com')

    input4 = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input')
    input4.send_keys('8-800-755-35-35')
    
    input5 = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input')
    input5.send_keys('Pushkina')

    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
