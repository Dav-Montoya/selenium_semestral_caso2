from funciones_selenium import *

pagina = "https://demo.testfire.net/"

try:
    abrir_chrome(pagina)
except Exception as e:
    print(f"error :{e}")