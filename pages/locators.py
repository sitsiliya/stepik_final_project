from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    PRODUCT_MAIN = (By.CSS_SELECTOR, "div.product_main>h1")
    MESSAGE_ABOUT_ADD_TO_BASKET = '//div[@id="messages"]/div[1]//strong'
    MESSAGE_ABOUT_PRODUCT_PRICE = '//div[@id="messages"]/div[3]'
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")