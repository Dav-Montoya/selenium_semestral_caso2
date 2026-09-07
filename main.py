from funciones_selenium import *

pagina = "https://demo.testfire.net/index.jsp"

try:
    
    ir_al_link(pagina)
    ini_sesion()
    con_saldo()
    con_tran()
    extraer_Tabla_a_Excel()
except Exception as e:
    print(f"error :{e}")