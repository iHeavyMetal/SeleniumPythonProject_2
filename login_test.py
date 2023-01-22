import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_log_in_passed(self):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    self.driver.get("http://seleniumdemo.com/")
    self.driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    self.driver.find_element(By.ID, "username").send_keys("HeavyMetal@gmail.com")
    self.driver.find_element(By.ID, "password").send_keys("Frytki123!")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)   #login by click ENTER_key
    #self.driver.find_element(By.XPATH, "//button[@class='woocommerce-Button button']").click()
    #self.driver.find_element(By.NAME, "login").click()

    assert self.driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
    time.sleep(5)

# def test_log_in_failed():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.maximize_window()
#     driver.get("http://seleniumdemo.com/")
#     driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
#     driver.find_element(By.ID, "username").send_keys("HeavyMetal@gmail.com")
#     driver.find_element(By.ID, "password").send_keys("Frytki123")
#     driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
#     assert "ERROR: Incorrect username or password." in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
#     time.sleep(5)