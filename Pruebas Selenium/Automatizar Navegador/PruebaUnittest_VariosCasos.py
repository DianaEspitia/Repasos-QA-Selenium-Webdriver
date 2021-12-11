import unittest
from selenium import webdriver

#Clase de prueba se debe heredar de Unittest
#Crear clase
class FindByIdName(unittest.TestCase):

    #Método - punto de entrada
    #Método para abrir el navegador y la página de prueba
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        url = "http://clouditeducation.com/pruebas/"
        driver.get(url)

    #Método para entontrar por id y nombre
    #NOTA: En Unittest la prueba debe comenzar con el nombre test
    def testId(self):
        elemento_id = driver.find_element_by_id("noImportante")
        if (elemento_id is not None):
            print("Elemento encontrado con el atributo id")

    def testName(self):
        elemento_name = driver.find_element_by_name("ultimo")
        if (elemento_name is not None):
            print("Elemento encontrado con el atributo name")

    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()
