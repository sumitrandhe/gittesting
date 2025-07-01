from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# import pdb
# pdb.set_trace()
try:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://stepupandlearn.in/wp-content/UI/javascript_alerts.html")
    # time.sleep(4)
    # search = driver.find_element(By.LINK_TEXT,"Sample URL")
    search = driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    search.click()
    time.sleep(5)


except Exception as e:
    print(str(e))
finally:
    driver.close()

