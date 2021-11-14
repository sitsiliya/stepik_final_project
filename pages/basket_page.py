from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_disappeared(self):
        assert self.is_disappeared(*BasketPageLocators.ITEMS_IN_BASKET), "Object is not disappeared"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "Items are in basket, but should not be"

    def should_be_message_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_BASKET_EMPTY), "There is not message about empty basket"