from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_message_product_add_to_basket(self):
        product_main = self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN).text
        message_about_add_to_basket=self.browser.find_element_by_xpath(ProductPageLocators.MESSAGE_ABOUT_ADD_TO_BASKET).text
        assert product_main == message_about_add_to_basket, "Product is not in the basket."

    def should_be_message_product_price(self):
        message_about_product_price = self.browser.find_element_by_xpath(ProductPageLocators.MESSAGE_ABOUT_PRODUCT_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_about_product_price, "Product cost is not correct."