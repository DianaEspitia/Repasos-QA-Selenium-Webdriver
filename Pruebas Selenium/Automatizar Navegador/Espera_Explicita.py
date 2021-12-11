import unittest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Clase de prueba se debe heredar de Unittest
#Crear clase
class EsperaExplicita(unittest.TestCase):

    #Método - punto de entrada
    #Método para abrir el navegador y la página de prueba
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        url = "http://clouditeducation.com/pruebas/"
        driver.get(url)
        driver.implicitly_wait(15)
        

    #Método para entontrar por id y nombre
    #NOTA: En Unittest la prueba debe comenzar con el nombre test

    def test1(self):
        espera = WebDriverWait(driver, 10) #Espera de 10 seg
        boton = espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="proceed"]')))

        if boton is not None:
            boton.click()
        
        time.sleep(3)


    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()