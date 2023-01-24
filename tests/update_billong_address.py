import time
from selenium.webdriver.common.by import By
import pytest

from pages.billing_address_page import BillingAddressPage
from pages.my_account_page import MyAccountPage
import random

@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:
    def test_update_billing_address(self):
        email = str(random.randint(1, 10000)) + "testtest123@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, 'Frytki123!')
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("Anon", "Anoni")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Moment", "00-666", "Something")
        billing_address_page.set_phone_number("666 666 666")
        billing_address_page.save_address()
        assert "Address changed successfully." in billing_address_page.get_message_text()

        time.sleep(2)