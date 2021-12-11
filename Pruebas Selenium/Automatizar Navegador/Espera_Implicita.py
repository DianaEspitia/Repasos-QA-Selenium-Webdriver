import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

#Clase de prueba se debe heredar de Unittest
#Crear clase
class DropDowMenu(unittest.TestCase):

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
        botonMenu = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/button')
        if botonMenu is not None:
            acciones = ActionChains(driver)
            acciones.move_to_element(botonMenu).perform() #perfom para realizar la acción

            link1 = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/a[1]')
            if link1 is not None:
                acciones.move_to_element(link1)
                acciones.click()
                acciones.perform()
        
        time.sleep(3)


    #Método para cerrar el navegador
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    #Ejecutar Unittest
    unittest.main()