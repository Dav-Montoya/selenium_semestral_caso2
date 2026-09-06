from selenium import webdriver
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

import openpyxl
import time


#driver_firefox = webdriver.Firefox()
#driver_edge = webdriver.Edge()
#driver_safari = webdriver.Safari()


def abrir_chrome (link):
    driver_chrome = webdriver.Chrome()
    driver_chrome.get(link)
    time.sleep(0.5)
    ver_pagina = driver_chrome.find_element(By.ID, "details-button")
    ver_pagina.click()
    time.sleep(1)
    ver_pagina = driver_chrome.find_element(By.ID, "proceed-link")
    ver_pagina.click()
    time.sleep(10)
    return driver_chrome

