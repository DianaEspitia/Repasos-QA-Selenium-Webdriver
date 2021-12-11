import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#Clase de prueba se debe heredar de Unittest
#Crear clase
class ClickSelect(unittest.TestCase):

    #Método - punto de entrada
    #Método para abrir el navegador y la página de prueba
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        url = "http://clouditeducation.com/pruebas/"
        driver.get(url)
        

    #Método para entontrar por id y nombre
    #NOTA: En Unittest la prueba debe comenzar con el nombre test

    def test1(self):
        frame = driver.find_element_by_xpath('//*[@id="pruebas-iframe"]')
        if frame is not None:
            driver.switch_to_frame(frame)
        
        nombre = driver.find_element_by_xpath('//*[@id="Segundo"]')
        if nombre is not None:
            nombre.send_keys("Diana")

        time.sleep(3)


    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()