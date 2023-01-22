import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:
    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("HeavyMetal@gmail.com", "Frytki123!")
        assert my_account_page.is_logout_link_displayed()
        time.sleep(5)

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("HeavyMetal@gmail.com1", "Frytki123!")
        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()
        time.sleep(5)
