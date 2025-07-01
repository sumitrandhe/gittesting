import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from file_handling import *

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
download = driver.find_element(By.LINK_TEXT, 'test.txt')
filepath = 'C:/Users/acer/Downloads/test.txt'

if check_file(filepath):
    remove_file(filepath)
    download.click()

filename = os.path.exists(filepath)
if filename:
    print("File downloaded successfully")

time.sleep(3)
driver.close() 