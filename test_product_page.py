import pytest
from .project.product_page import ProductPage
from .project.base_page import BasePage
import time


@pytest.mark.skip
def  test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
    page =  ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницуc
    page.setup_all_cases()
    
    
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
    page =  ProductPage(browser, link)   
    page.open()                      
    page.setup_error_when_see_success_message()
    
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
    page =  ProductPage(browser, link)   
    page.open()                      
    page.setup_no_succcess_without_adding_item()
    

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
    page =  ProductPage(browser, link)   
    page.open()                      
    page.setup_succcess_message_disappear()

@pytest.mark.skip    
def test_guest_can_go_to_login_page_from_product_page(browser):
    #'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
    page =  ProductPage(browser, link)   
    page.open()                      
    page.setup_check_link_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
    page =  ProductPage(browser, link)   
    page.open()                      
    page.setup_go_to_empty_cart()
