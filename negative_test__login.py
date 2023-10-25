import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

time.sleep(5)

driver.quit()


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def test_run(self):
        self.driver.quit()

    def test_run_2(self):
        time.sleep(5)

    def test_negative_username(self):
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.ID, "username")
        ))
        username_field.send_keys("incorrectUser ")

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")
        text = password_field.is_displayed()

        submit_buton = self.driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_buton.click()

        time.sleep(5)

        expected_url = "https://practicetestautomation.com/practice-test-login/"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, "Your username is invalid!"

    def tearDown(self):
        self.driver.quit()
