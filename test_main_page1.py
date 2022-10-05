import pytest
from .project.product_page import ProductPage




def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):#
    link = 'http://selenium1py.pythonanywhere.com/ru/'
    page = ProductPage(browser, link)   
    page.open()                      
    page.setup_go_to_empty_cart()
    