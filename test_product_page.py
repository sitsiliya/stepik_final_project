from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.xfail
@pytest.mark.parametrize('offer_id', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer_id):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_id}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_message_product_add_to_basket()
    page.should_be_message_product_price()