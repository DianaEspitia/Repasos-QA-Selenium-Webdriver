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
        filas = driver.find_elements(By.XPATH, '//tr')
        if (filas is not None):
            tam_elementos = len(filas)
            print("Elemento encontrado con //tr")
            print("La cantidad de elementos //tr que hay es {}".format(tam_elementos))

    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()