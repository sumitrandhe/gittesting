from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://stepupandlearn.in/wp-content/UI/dropdown.html")
driver.implicitly_wait(5)
drop_element =driver.find_element(By.XPATH, "//select[@id='dropdown']")

drop_options = Select(drop_element)

# drop_options.select_by_visible_text("Python")
# drop_options.select_by_index(0)
drop_options.select_by_value("3")
time.sleep(3)

driver.close()





#import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# try:
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://gokcecapital.com/free-land/")
#     # driver.implicitly_wait(5)
#
#     # time.sleep(5)
#     waitobj = WebDriverWait(driver, 15)
#     button = waitobj.until( EC.presence_of_element_located((By.XPATH, '//div[@id="bottom-box-text-p-mobile" and text()=" Grab Your "]//a[text()="Dream Land at Unbelievable Prices"]')))
#     # button.click()
#     print(button.is_displayed())
# except Exception as e:
#     print(str(e))
# finally:
#     driver.close()


# button = waitobj.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[name='start']"))) #We directly locate element in button


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# waitobj = WebDriverWait(driver,19)
# button = waitobj.until(EC.presence_of_element_located(By.XPATH,""))


# from selenium import webdriver
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.implicitly_wait(4)
# button = driver.find_element(By.CSS_SELECTOR, "button.start")
# button.click()
# print(button.is_displayed())
# driver.close()



# def check_nav(url1, url2):
#     try:
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         driver.get(url1)
#         if "stepupandlearn" in url1:
#             driver.get("https://youtube.com/")
#             if "youtube" in url2:
#                 return True
#             else:
#                 return False
#     except Exception as e:
#         print(e)
#     finally:
#         driver.close()


# def check_myurl(url2, link_text):
#     try:
#         d = webdriver.Chrome()
#         d.get(url2)
#         d.maximize_window()
#         if link_text in d.current_url:
#             time.sleep(5)
#             return True
#         else:
#             # print(False)
#             return False
#             time.sleep(5)
#     except Exception as e:
#         print(str(e))
#     finally:
#         d.close()