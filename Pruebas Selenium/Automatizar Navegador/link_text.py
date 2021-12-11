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
    def testText(self):
        elemento_text = driver.find_element_by_link_text('Pagina 2')
        if (elemento_text is not None):
            print("Elemento encontrado con link text = Pagina 2")

    def testPartialText(self):
        elemento_partial_text = driver.find_element_by_partial_link_text("ink")
        if (elemento_partial_text is not None):
            print("Elemento encontrado con el texto parcial ink")

    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()