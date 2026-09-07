from selenium import webdriver
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import openpyxl
import time


#driver_firefox = webdriver.Firefox()
#driver_edge = webdriver.Edge()
#driver_safari = webdriver.Safari()
driver = webdriver.Chrome()
def abrir_chrome():
    driver = webdriver.Chrome()

def ir_al_link (link):
    driver.get(link)
    time.sleep(0.5)
    ver_pagina = driver.find_element(By.ID, "details-button")
    ver_pagina.click()
    time.sleep(1)
    ver_pagina = driver.find_element(By.ID, "proceed-link")
    ver_pagina.click()
    time.sleep(1)     

def intr_datos():
    #introducir datos en el login
    #Se buscan los elementos por ID
    time.sleep(1)
    box_nombre = driver.find_element(By.ID, "uid")
    box_nombre.send_keys("jsmith")

    box_psw = driver.find_element(By.ID, "passw")
    box_psw.send_keys("demo1234")
    #enviar datos
    box_psw.submit()    

def ini_sesion ():
    btn_signin = driver.find_element(By.ID, "LoginLink")
    btn_signin.click()
    time.sleep(1)
    intr_datos()
    time.sleep(1)

def con_saldo ():
    btn_acc_smry = driver.find_element(By.ID, "MenuHyperLink1")
    

    btn_acc_smry.click()
    time.sleep(3)
    combo_box = driver.find_element(By.ID, "listAccounts")
    combo_box.click()
    select = Select(combo_box)
    select.select_by_visible_text("800002 Savings")
    time.sleep(10)
    btn_go = driver.find_element(By.ID, "btnGetAccount")
    btn_go.click()
    time.sleep(10)


def con_mov ():
    btn_acc_mvm = driver.find_element(By.ID, "MenuHyperLink2")
    btn_acc_mvm.click()