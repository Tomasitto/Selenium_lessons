from lib2to3.pgen2 import driver
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locator import ItemLocator, ProductPageLocators
import time


class ProductPage(BasePage):

    def setup_all_cases(self):
        self.click_to_add_item()
        self.solve_quiz_and_get_code()
        self.go_to_cart()
        self.should_same_item_be_in_cart()

    def setup_error_when_see_success_message(self):
        self.click_to_add_item()
        self.solve_quiz_and_get_code()
        self.should_not_be_success_message()

    def setup_no_succcess_without_adding_item(self):
        self.should_not_be_success_message()

    def setup_succcess_message_disappear(self):
        self.click_to_add_item()
        self.solve_quiz_and_get_code()
        self.should_wait_success_message()

    def setup_check_link_to_login_page(self):
        self.should_go_to_login_page()
        self.shoud_be_login_page()


    def setup_go_to_empty_cart(self):
        self.go_to_cart()
        self.can_go_to_cart_page()
        self.check_empty_cart_page()

    def click_to_add_item(self):
        login_link = self.browser.find_element(*ItemLocator.ADD_BUTTON)
        self.name_of_book = self.browser.find_element(*ItemLocator.BOOK_NAME).text
        self.price_of_book = self.browser.find_element(*ItemLocator.PRICE_OF_ITEM).text
        login_link.click() 

    def go_to_cart(self):
        login_link = self.browser.find_element(*ItemLocator.LINK_TO_CART)
        login_link.click() 

    def should_same_item_be_in_cart(self):
        item_in_cart = self.browser.find_element(*ItemLocator.ITEM_IN_CART).text
        assert self.name_of_book == item_in_cart, 'Different items in cart'

    def should_be_same_price_of_item_in_cart(self):
        item_in_cart = self.browser.find_element(*ItemLocator.PRICE_OF_ITEM_IN_CART).text
        assert self.price_of_book == item_in_cart, 'Different prices in cart'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_wait_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_go_to_login_page(self):
        login_link = self.browser.find_element(*ItemLocator.LINK_TO_SIGNUP)
        login_link.click()

    def shoud_be_login_page(self):
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/ru/accounts/login/', "can't get to Log In page"

    def can_go_to_cart_page(self):
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/ru/basket/', "can't get Basket page"

    def check_empty_cart_page(self):
        empty_cart = self.browser.find_element(*ItemLocator.EMPTY_CART).text
        print(empty_cart)
        assert empty_cart == 'Корзина', 'The Basket is not empty'