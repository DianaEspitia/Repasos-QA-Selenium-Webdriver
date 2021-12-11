from selenium import webdriver

driver = webdriver.Chrome()
url = "http://clouditeducation.com/pruebas/"
driver.get(url)

elemento_id = driver.find_element_by_id("noImportante")
if (elemento_id is not None):
    print("Elemento encontrado con el atributo id")

elemento_name = driver.find_element_by_name("ultimo")
if (elemento_name is not None):
    print("Elemento encontrado con el atributo name")

driver.quit()