import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Test_Cases.test_base_claass import Base_Test
class Test_Login(Base_Test):

    def test_login(self):

     self.driver.get("https://cosmos.angelbroking.com/login/")
     print(self.driver.title)
     # set of credentials of user as a dectionary
     credentials = {'admin@gmail.com':'test12345', 'admint2@gmail.com':'Test@12345', 'nagendra@scaledesk.xyz':'Test@12345'}
     for k in credentials:
        uname = self.driver.find_element(By.XPATH, "//input[@id='id_email']")
        uname.clear()
        uname.send_keys(k)
        for v in credentials:
            passwrd = self.driver.find_element(By.XPATH, "//input[@name='password']")
            passwrd.send_keys(v)
            break

     login = self.driver.find_element(By.XPATH, "//button[@type='submit']")
     login.click()
     print("Due to failure of captcha verification login is not successfull")
