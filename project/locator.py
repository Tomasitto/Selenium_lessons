from selenium.webdriver.common.by import By

class ItemLocator:
    ADD_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    LINK_TO_CART = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    ITEM_IN_CART = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[2]/h3/a')
    PRICE_OF_ITEM = (By.CLASS_NAME, 'price_color')
    PRICE_OF_ITEM_IN_CART = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[4]/p')