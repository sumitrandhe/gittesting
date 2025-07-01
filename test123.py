from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

element = driver.find_element(By.LINK_TEXT,"Home")
print(element.is_displayed())

driver.close()



"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
file_upload = driver.find_element(By.XPATH,"//input[@id='file-upload']")
upload_btn = driver.find_element(By.XPATH,"//input[@id='file-submit' and @value='Upload']")
print(upload_btn.is_displayed())
file_upload.send_keys("C:/Users/acer/Desktop/the-magic-check-en.pdf")
time.sleep(5)
upload_btn.click()
time.sleep(5)
driver.close()
"""

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://stepupandlearn.in/wp-content/UI/windows.html")
time.sleep(2)
# driver.switch_to.new_window("tab")
# driver.get("https://stepupandlearn.in/")
# time.sleep(2)
# driver.switch_to.new_window("tab")
# driver.get("https://youtube.in/")
select_element = driver.find_element(By.XPATH,"//a[text()='Click Here']")
# driver.switch_to.new_window("tab")
select_element.click()

time.sleep(5)


# driver.close()
driver.quit()
"""


"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://stepupandlearn.in/wp-content/UI/windows.html")
driver.maximize_window()
driver.implicitly_wait(3)
time.sleep(4)
locator = driver.find_element(By.XPATH,"//a[contains(text(),'Click Here')]")
locator.click()
l1 = driver.window_handles #collect unique id's of all the windows in l1


# driver.switch_to.window(l1[0]) #switching to window at 0th location
# print(driver.title,driver.current_url)
# time.sleep(3)
# driver.switch_to.window(l1[1]) #switching to window at 1th location
# print(driver.title,driver.current_url)

for i in l1:
    print(driver.title, driver.current_url)
    driver.switch_to.window(i)
    print(driver.title, driver.current_url)



time.sleep(3)

driver.close()
"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.amazon.in/ref=nav_logo")
driver.maximize_window()
# Scroll down by down arrow in keyboard
element = driver.find_element(By.TAG_NAME,'body')
# element.send_keys(Keys.PAGE_DOWN)
#almost all keyboard keys are available in common.keys
element.send_keys(Keys.DOWN)
# element.send_keys(Keys.UP)
# element.send_keys(Keys.LEFT)
time.sleep(5)
"""


"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from file_handling import *

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
download = driver.find_element(By.LINK_TEXT,'testfile.txt')
filepath = 'C:/Users/acer/Downloads/testfile.txt'

if check_file(filepath):
    remove_file(filepath)

download.click()
filename = os.path.exists(filepath)
if filename:
    print("File downloaded successfully")

time.sleep(3)
driver.close()"""








