import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:\Users\sowen\OneDrive\Documents\Python\Selenium\Setup"
driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)
uname = driver.find_element(By.ID,'user-name')
pword = driver.find_element(By.ID,'password')
login = driver.find_element(By.ID,'login-button')

uname.send_keys('standard_user')
pword.send_keys('secret_sauce')
time.sleep(3)
login.click()
time.sleep(5)