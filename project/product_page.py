from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locator import ItemLocator


class ProductPage(BasePage):

    def setup_all_cases(self):
        self.click_to_add_item()
        self.solve_quiz_and_get_code()
        self.go_to_cart()
        self.should_same_item_be_in_cart()
        self.should_be_same_price_of_item_in_cart

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
