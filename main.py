from funciones_selenium import *

pagina = "https://demo.testfire.net/index.jsp"

try:
    abrir_chrome()
    ir_al_link(pagina)
    ini_sesion()
    con_saldo()
    con_tran()
except Exception as e:
    print(f"error :{e}")