import unittest
from selenium import webdriver

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
    def testXPath(self):
        elemento_xpath = driver.find_element_by_xpath('//tr[@id="importante"]')
        if (elemento_xpath is not None):
            print("Elemento encontrado con el XPath")

    def testClass(self):
        elemento_class = driver.find_element_by_class_name("rojo")
        if (elemento_class is not None):
            print("Elemento encontrado con la clase name = rojo")

    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()