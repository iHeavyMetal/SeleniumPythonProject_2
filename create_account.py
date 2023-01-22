import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random

def test_create_account_failed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys("testtest123@gmail.com")
    driver.find_element(By.ID, "reg_password").send_keys("Frytki123!")
    driver.find_element(By.NAME, "register").click()
    msg = "Error: An account is already registered with your email address. Please log in."
    assert msg in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text

def test_create_account_passed():
    email = str(random.randint(1, 10000)) + "testtest123@gmail.com"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("Frytki123!")
    driver.find_element(By.NAME, "register").click()
    msg = "Error: An account is already registered with your email address. Please log in."
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
    time.sleep(2)