from selenium_revision.revision import *
from selenium_revision.first import  *
from selenium.webdriver.common.by import By
import time


def test_1(setup1):
    all1 = "//input[@name='language']"
    l1 = setup1.find_elements(By.XPATH, all1)
    l1[0].click()


def test_2(setup1):
    all1 = "//input[@name='language']"
    l1 = setup1.find_elements(By.XPATH, all1)
    l1[1].click()


def test_3(setup1):
    all1 = "//input[@name='language']"
    l1 = setup1.find_elements(By.XPATH, all1)
    l1[2].click()


def test_4(setup1):
    all1 = "//input[@name='language']"
    l1 = setup1.find_elements(By.XPATH, all1)
    l1[3].click()