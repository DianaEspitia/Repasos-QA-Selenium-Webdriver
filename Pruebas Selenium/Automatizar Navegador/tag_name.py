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
    def testTagName(self):
        elemento_tag_name = driver.find_element_by_tag_name('h3')
        if (elemento_tag_name is not None):
            print("Elemento encontrado con el tag name h3")

    def testCss(self):
        elemento_css = driver.find_element_by_css_selector("#primera")
        if (elemento_css is not None):
            print("Elemento encontrado con el css selector = #primera")

    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()