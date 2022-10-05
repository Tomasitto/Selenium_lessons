import pytest
from .project.product_page import ProductPage
from .project.base_page import BasePage
import time



def  test_guest_can_add_product_to_basket(browser, link):
    link = link
    page =  ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницуc
    page.setup_all_cases()
    time.sleep(5)
    

    
