from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class EditarProductoPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    localizador_campo_codigo = (By.ID,"id_codigo")
    localizador_campo_nombre = (By.ID,"id_nombre")
    localizador_campo_descripcion = (By.ID,"id_descripcion")
    localizador_campo_cantidad_minima = (By.ID,"id_cantidad_minima")
    localizador_campo_precio = (By.ID,"id_precio")
    localizador_boton_editar = (By.ID,"btnEdit")
    alerta_campo_incorrecto = (By.CSS_SELECTOR, '.alert > span:nth-child(1)')

    def abrir(self, url):
        self.driver.get(url)

    def ingresar_codigo(self, codigo):
        campo_codigo = self.wait.until(EC.element_to_be_clickable(self.localizador_campo_codigo))
        campo_codigo.clear()
        campo_codigo.send_keys(codigo)
    
    def ingresar_nombre(self, nombre):
        campo_nombre = self.wait.until(EC.element_to_be_clickable(self.localizador_campo_nombre))
        campo_nombre.clear()
        campo_nombre.send_keys(nombre)

    def ingresar_descripcion(self, descripcion):
        campo_descripcion = self.wait.until(EC.element_to_be_clickable(self.localizador_campo_descripcion))
        campo_descripcion.clear()
        campo_descripcion.send_keys(descripcion)

    def ingresar_cantidad_minima(self, cantidad_minima):
        campo_cantidad_minima = self.wait.until(EC.element_to_be_clickable(self.localizador_campo_cantidad_minima))
        campo_cantidad_minima.clear()
        campo_cantidad_minima.send_keys(cantidad_minima)

    def ingresar_precio(self, precio):
        campo_precio = self.wait.until(EC.element_to_be_clickable(self.localizador_campo_precio))
        campo_precio.clear()
        campo_precio.send_keys(precio)

    def editar(self):
        self.wait.until(EC.element_to_be_clickable(self.localizador_boton_editar)).click()

    def recuperar_alerta(self):
        alerta = self.wait.until(EC.visibility_of_element_located(self.alerta_campo_incorrecto))
        return alerta.text