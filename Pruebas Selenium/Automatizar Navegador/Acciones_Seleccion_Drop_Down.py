import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

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

    #Menú desplegable
    def test1(self):
        ingredientes = driver.find_element_by_name("ingrediente")
        if (ingredientes is not None):
            ingredientesSelect = Select(ingredientes)
            ingredientesSelect.select_by_value("cilantro")      
        time.sleep(5)

        print("Prueba 1 ejecutada con éxito")

    #Opción múltiple
    def test2(self):
        frutas = driver.find_element_by_name("Select1")
        if (frutas is not None):
            frutasSelect = Select(frutas)
            frutasSelect.select_by_index("1")  
            frutasSelect.select_by_visible_text("Sandia")  
        time.sleep(5)

        print("Prueba 2 ejecutada con éxito")

    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()