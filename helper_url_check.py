from selenium import webdriver
import time

def check_url_title(url,title = None, current_url = None):
    try:
        # import pdb
        # pdb.set_trace()
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        # time.sleep(2)
        if title:
            return driver.title
        elif current_url:
            return driver.current_url

        # if title:
        #     if driver.title == "The Internet" :
        #         return True
        #     else:
        #         return False
        # elif current_url:
        #     if "internet" in driver.current_url:
        #         return True
        #     else:
        #         return False

    except Exception as e:
        return False
    finally:
        driver.close()



