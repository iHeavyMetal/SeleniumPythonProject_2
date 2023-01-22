import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_update_billing_address():
    email = str(random.randint(1, 10000)) + "testtest123@gmail.com"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("Frytki123!")
    driver.find_element(By.NAME, "register").click()
    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.LINK_TEXT, "Edit").click()
    driver.find_element(By.ID, "billing_first_name").send_keys("Anon")
    driver.find_element(By.ID, "billing_last_name").send_keys("Anoni")
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Poland")
    driver.find_element(By.ID, "billing_address_1").send_keys("Manowar")
    driver.find_element(By.ID, "billing_postcode").send_keys(("00-666"))
    driver.find_element(By.ID, "billing_city").send_keys("Valhalla ")
    driver.find_element(By.ID, "billing_phone").send_keys("666 666 666")
    #driver.find_element(By.NAME, "save_address").click() #another way to click 'Save Address", can find also by value='Save address'
    driver.find_element(By.XPATH, "//button[@name='save_address']").click()
    assert "Address changed successfully." in driver.find_element(By.XPATH, "//div[@class='woocommerce-message']").text

    time.sleep(2)