import time
from selenium.webdriver.common.by import By
from selenium import  webdriver
from popup_locator import popup_locator_dict

def check_alert(loc,result_text=None):
    try:
        driver = webdriver.Firefox()
        driver.get("https://stepupandlearn.in/wp-content/UI/javascript_alerts.html")
        driver.maximize_window()
        time.sleep(3)
        element = driver.find_element(By.XPATH,popup_locator_dict.get(loc))
        element.click()
        popup_alert = driver.switch_to.alert
        popup_alert.accept()
        time.sleep(3)
        result = "//p[@id='result']"
        actual_result = driver.find_element(By.XPATH,result)
        time.sleep(3)

        if result_text:
            print( actual_result.text )
            if actual_result.text == result_text:
                return True
            else:
                return False
    except Exception as e:
        print(str(e))
    finally:
        driver.close()


def check_popup_alert(loc,accept=None,dismiss=None,result_text=None):
    try:
        driver = webdriver.Firefox()
        driver.get("https://stepupandlearn.in/wp-content/UI/javascript_alerts.html")
        driver.maximize_window()
        time.sleep(3)
        element = driver.find_element(By.XPATH,popup_locator_dict.get(loc))
        element.click()
        popup_alert = driver.switch_to.alert
        if accept:
            popup_alert.accept()
            time.sleep(3)
        elif dismiss:
            popup_alert.dismiss()
            time.sleep(3)

        result = "//p[@id='result']"
        actual_result = driver.find_element(By.XPATH,result)
        time.sleep(3)

        if result_text:
            if actual_result.text == result_text:
                return True
            else:
                return False
    except Exception as e:
        print(str(e))
    finally:
        driver.close()

