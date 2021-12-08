import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

GOOGLE_FORM_LINK = os.environ.get("your_google_form_link")


class FormFilling:
    def __init__(self, path):
        # driver path
        self.chrome_driver_path = Service(path)
        # driver object
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)

    def open_form(self, addr, cost, url):
        # opening google form
        self.driver.get(GOOGLE_FORM_LINK)
        time.sleep(3)

        # putting address in address field
        put_address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]'
                                                         '/div/div[1]/div/div[1]/input')
        put_address.send_keys(addr)

        # putting price in a field
        time.sleep(2)
        put_price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/'
                                                       'div/div[1]/div/div[1]/input')
        put_price.send_keys(cost)

        # putting link in a field
        time.sleep(2)
        put_link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
                                                      '/div/div[1]/div/div[1]/input')
        put_link.send_keys(url)

        submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit_button.click()

