#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:24:42 2021

@author: leoprimero
"""

url_1 =  'https://auth.afip.gob.ar/contribuyente_/login.xhtml'

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='/home/leoprimero/Documentos/Programas/Programas_Python/chromedriver')
driver.get(url_1)
user = 'CUIL/CUIT'     
password = 'Clave Fiscal'   
original_window = driver.current_window_handle
driver.find_element(By.XPATH,'//input[@name="F1:username"]').send_keys(user)
driver.find_element(By.XPATH, '//input[@class="btn btn-success full-width"]').click() 
imput_password = driver.find_element(By.XPATH,'//input[@name="F1:password"]').send_keys(password)
driver.find_element(By.XPATH, '//input[@class="btn btn-success full-width"]').click()
sleep(3)
assert len(driver.window_handles) == 1
window_before = driver.window_handles[0]

try:
    driver.find_element_by_xpath('//*[@id="j_idt49"]/div/div[2]/div[2]/div[1]/ul/li[10]/a/p').click()
    sea = True
except:
    driver.find_element_by_xpath('//*[@id="cardGoPortalFull"]/div/div/div/b/a').click()
    sea = False 
sleep(3)

if sea == False:
    driver.find_element_by_xpath('//*[@id="root"]/div/main/section[1]/div/ul/li[3]/a/i').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/section[2]/div/div/div[31]/div/div/div/div[2]/h4').click()
    sleep(3)
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
# sleep(5)

driver.find_element(By.XPATH,'//*[@id="tableContent"]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/div/div/div/div/div/input[2]').click()
driver.find_element(By.XPATH, '//*[@id="menu_consultaddjj"]/u').click()


menu=Select(driver.find_element(By.XPATH, '//select[@name="usuarioCuit"]'))
menu.select_by_visible_text(user)

menu2=Select(driver.find_element(By.XPATH, '//select[@name="contribuyenteCuit"]'))
menu2.select_by_visible_text(user)

mes=Select(driver.find_element(By.XPATH, '//select[@name="periodoFiscalMonth"]'))
mes.select_by_visible_text('8')

year=Select(driver.find_element(By.XPATH, '//select[@name="periodoFiscalYear"]'))
year.select_by_visible_text("2021")

driver.find_element(By.XPATH, '//input[@class="btn btn-sm btn-primary"]').click()

driver.find_element(By.XPATH, '//*[@id="consultaDjTable"]/tbody/tr/td[4]/center/form/a').click()
# sleep(5)
driver.find_element(By.XPATH, '//input[@class="btn btn-sm btn-primary"]').click()

# if wondows_handles[i>2]:
#     try:
#         driver.find_element_by_xpath('//*[@id="j_idt49"]/div/div[2]/div[2]/div[1]/ul/li[10]/a/p').click()
#         sea = True
#     except:
#         driver.find_element_by_xpath('//*[@id="cardGoPortalFull"]/div/div/div/b/a').click()
#         sea = False 

assert len(driver.window_handles) == 2
try:
    window_pop_up = driver.window_handles[2]
    window_pop_up = driver.window_handles[2]
    driver.close()
    driver.switch_to_window(window_after)
except:
    ()

# window_pop_up = driver.window_handles[2]   #Acá hay un problema
# driver.switch_to_window(window_pop_up)
# driver.close()
# driver.switch_to_window(window_after)
sleep(2)

driver.find_element(By.XPATH, '//*[@id="consultaDjTable"]/tbody/tr/td[4]/center/form/a').click()
driver.find_element(By.XPATH, '//input[@title="Siguiente"]').click()
driver.find_element(By.XPATH, '//input[@title="Siguiente"]').click()


sleep(5)


## Acá elejimos en donde desea realizar el pago

# pagar   el primero
# element
#     <input id="edp1001" type="image" src="../img/content/pago/edp/edp1001.gif" onclick="document.forms[0].entidadId.value=1001;
#                      document.forms[0].nombreEdp.value='RED LINK';
#                      document.forms[0].esPidePagadorCuit.value='S';" class="edpeffectbutton" style="">

# path 
# //*[@id="edp1001"]

# pago mis cuentas  el segundo 
# element
# <input id="edp1002" type="image" src="../img/content/pago/edp/edp1002.gif" onclick="document.forms[0].entidadId.value=1002;
#                       document.forms[0].nombreEdp.value='BANELCO';
#                       document.forms[0].esPidePagadorCuit.value='S';" class="edpeffectbutton" style="">

# driver.find_element(By.XPATH, '//*[@id="edp1002"]').click()  #PAGOMISCUENTAS

# driver.find_element(By.XPATH, '//*[@id="idyesbutton"]').click()




                    
# path  
# //*[@id="edp1002"]

# inter banquing el tercer 
# element 
# <input id="edp1003" type="image" src="../img/content/pago/edp/edp1003.gif" onclick="document.forms[0].entidadId.value=1003;
#                      document.forms[0].nombreEdp.value='INTERBANKING';
#                      document.forms[0].esPidePagadorCuit.value='S';" class="edpeffectbutton" style="">
                     
# path 
# //*[@id="edp1003"]

# xn group 
# element
# <input id="edp1005" type="image" src="../img/content/pago/edp/edp1005.gif" onclick="document.forms[0].entidadId.value=1005;
#                      document.forms[0].nombreEdp.value='XNET - SUCURSAL BANCARIA';
#                      document.forms[0].esPidePagadorCuit.value='N';" class="edpeffectbutton" style="">
    
# path 
# //*[@id="edp1005"]



####   DESPUES NOS APARECE UN POP UP QUE DICE SI ESTAMOS SEGUROS 

# PAGO MIS CUENTAS 
# ELEMENTO
# <input type="button" class="btn btn-sm btn-primary" id="idyesbutton" onblur="Dialog.win[2].okFocus()" value="Sí" onclick="Dialog.win[2].callButtonFunctionCallback(3)">
# PATH
# //*[@id="idyesbutton"]

# PAGAR 
# ELEMENTO
# <input type="button" class="btn btn-sm btn-primary" id="idyesbutton" onblur="Dialog.win[3].okFocus()" value="Sí" onclick="Dialog.win[3].callButtonFunctionCallback(3)">
# PATH 
# //*[@id="idyesbutton"]

# INTERBANKING
# ELEMENTO
# <input type="button" class="btn btn-sm btn-primary" id="idyesbutton" onblur="Dialog.win[4].okFocus()" value="Sí" onclick="Dialog.win[4].callButtonFunctionCallback(3)">
# PATH
# //*[@id="idyesbutton"]

# XN GROUP 
# ELEMENTO
# <input type="button" class="btn btn-sm btn-primary" id="idyesbutton" onblur="Dialog.win[5].okFocus()" value="Sí" onclick="Dialog.win[5].callButtonFunctionCallback(3)">
# PATH 
# //*[@id="idyesbutton"]

print('EL PROGRAMA HA FINALIZADO POR AHORA')


###  EXPORTAR DETALLE A PDF

# <i class="fa fa-file-pdf-o"></i>
