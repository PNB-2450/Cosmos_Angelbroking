import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Test_Cases.test_base_claass import Base_Test


class Test_Cosmos_Registration(Base_Test):
    def test_registration(self):
        self.driver.get("https://cosmos.angelbroking.com/")
        print(self.driver.title)
        #click on Register button
        reg_btn = self.driver.find_element(By.XPATH, "//ul[@class='navbar-nav ml-auto align-items-center']/li[5]")
        reg_btn.click()

#       Enter Full name
        full_name = self.driver.find_element(By.XPATH, "//input[@name='full_name']")
        full_name.send_keys('Nagendra')

        # Enter email
        email = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email.send_keys('pn.babu0@gmail.com')
        #Eter mobile number
        mobile_number = self.driver.find_element(By.XPATH, "//input[@name='mobile']")
        mobile_number.send_keys("9494902450")
        #Enter Password
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys('Test@12345')
        #Click on submit button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Due to failure of captcha verification login is not successfull")




