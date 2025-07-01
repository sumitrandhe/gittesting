import time
from logging import raiseExceptions
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class SelectOptions:
    def __init__(self):
        self.url = "https://stepupandlearn.in/wp-content/UI/dropdown.html"
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.driver.maximize_window()

    def select_by_text(self,text):
        try:
            drop_element = self.driver.find_element(By.ID,"dropdown")
            drop_option = Select(drop_element)
            select_option = drop_option.select_by_visible_text(text=text)
            self.driver.save_screenshot(f"select{text}.png")
            return True
        except Exception as e:
            raise ValueError("exp")
        finally:
            time.sleep(2)
            self.driver.close()

    def select_by_index(self,i):
        try:
            drop_element = self.driver.find_element(By.ID,"dropdown")
            drop_option = Select(drop_element)
            select_option = drop_option.select_by_index(i)
            self.driver.save_screenshot(f"select{i}.png")
            return True
        except Exception as e:
            raise ValueError("exp")
        finally:
            time.sleep(2)
            self.driver.close()

    def select_by_value(self,val):
        try:
            drop_element = self.driver.find_element(By.ID,"dropdown")
            drop_option = Select(drop_element)
            select_option = drop_option.select_by_value(val)
            self.driver.save_screenshot(f"select{val}.png")
            return True
        except Exception as e:
            raise ValueError("exp")
        finally:
            time.sleep(2)
            self.driver.close()


# obj1 = SelectOptions()
# obj1.select_by_text("Java")
# obj1.select_by_index(3)
# obj1.select_by_value("4")