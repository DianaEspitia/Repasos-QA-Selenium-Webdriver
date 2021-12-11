import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#Clase de prueba se debe heredar de Unittest
#Crear clase
class FindBy(unittest.TestCase):

    #Método - punto de entrada
    #Método para abrir el navegador y la página de prueba
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        url = "http://clouditeducation.com/pruebas/"
        driver.get(url)

    #Método para entontrar por id y nombre
    #NOTA: En Unittest la prueba debe comenzar con el nombre test
    def testElement(self):
        elemento = driver.find_element(By.XPATH, '//*[@id="noImportante"]')
        if (elemento is not None):
            print("Elemento encontrado con XPath")

    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()