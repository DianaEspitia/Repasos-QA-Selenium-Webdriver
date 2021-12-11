import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Clase de prueba se debe heredar de Unittest
#Crear clase
class ClickBotonesYCasillas(unittest.TestCase):

    #Método - punto de entrada
    #Método para abrir el navegador y la página de prueba
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        url = "http://clouditeducation.com/pruebas/"
        driver.get(url)
        

    #Método para entontrar por id y nombre
    #NOTA: En Unittest la prueba debe comenzar con el nombre test
    def testBotonesCasillas(self):
        casilla = driver.find_element(By.XPATH, '//*[@id="CheckboxGroup1_0"]')
        if (casilla is not None):
            casilla.click()           
          
        time.sleep(1)
        
        boton = driver.find_element(By.XPATH, '//*[@id="RadioGroup1_0"]')
        if (boton is not None):
            boton.click()  
        
        time.sleep(1)

        print("Prueba ejecutada con éxito")

    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()