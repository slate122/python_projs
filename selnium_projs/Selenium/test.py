import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:\Users\sowen\OneDrive\Documents\Python\Selenium\Setup"
driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/download")
driver.implicitly_wait(3)
my_element = driver.find_element(By.LINK_TEXT,"some-file.txt") 
my_element.click()
time.sleep(5)