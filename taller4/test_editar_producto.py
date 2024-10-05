import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import HtmlTestRunner
from editar_producto_page import EditarProductoPage
import os
import sys
import django
#Agregar la ruta del directtorio del proyecto Django al PYTHONPATH
sys.path.append(r"D:\Automatizacion\Semana04\taller\proyecto\miproyecto")
#Configurar la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miproyecto.settings')
# Inicializar Django
django.setup()
from producto.models import Producto
import logging
logging.basicConfig(level=logging.INFO)
logging.info("test_editar_producto")

class EditarProductoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.url_base = "http://127.0.0.1:9000/productos"
        cls.EditarPage = EditarProductoPage(cls.driver)
        Producto.objects.all().delete()
        nuevo_producto = Producto(codigo="00000011", nombre="radio", descripcion="radio FM", cantidad_minima=3, precio=34.00)
        nuevo_producto.save()
        cls.producto_inicial = Producto.objects.get(codigo="00000011")
        
    def setUp(self):
        self.EditarPage.abrir(f"{self.url_base}/editar/{self.producto_inicial.id}")

    def test_editar_codigo_incorrecto(self):
        try:
            driver = self.driver
            driver.get(f"{self.url_base}/editar/{self.producto_inicial.id}")
            pagina_editar = self.EditarPage
            codigo_producto = "0000001"
            nombre_producto = "Actualizado"
            descripcion_producto = "Actualizado FM"
            cantidad_producto = 1
            precio_producto = 23.89

            pagina_editar.ingresar_codigo(codigo_producto)
            pagina_editar.ingresar_nombre(nombre_producto)
            pagina_editar.ingresar_descripcion(descripcion_producto)
            pagina_editar.ingresar_cantidad_minima(cantidad_producto)
            pagina_editar.ingresar_precio(precio_producto)
            pagina_editar.editar()

            self.assertNotEqual(self.url_base, driver.current_url)
            texto_esperado = pagina_editar.recuperar_alerta()
            self.assertEqual('', texto_esperado)
        except Exception as e:
            self.fail(f"No se puede continuar con la actualizacion debido a un problema en el campo {texto_esperado}")

    def test_editar_nombre_incorrecto(self):
        try:
            driver = self.driver
            driver.get(f"{self.url_base}/editar/{self.producto_inicial.id}")
            pagina_editar = self.EditarPage
            codigo_producto = "00000012"
            nombre_producto = "a"
            descripcion_producto = "Actualizado FM"
            cantidad_producto = 1
            precio_producto = 23.89

            pagina_editar.ingresar_codigo(codigo_producto)
            pagina_editar.ingresar_nombre(nombre_producto)
            pagina_editar.ingresar_descripcion(descripcion_producto)
            pagina_editar.ingresar_cantidad_minima(cantidad_producto)
            pagina_editar.ingresar_precio(precio_producto)
            pagina_editar.editar()

            self.assertNotEqual(self.url_base, driver.current_url)
            texto_esperado = pagina_editar.recuperar_alerta()
            self.assertEqual('', texto_esperado)
        except Exception as e:
            self.fail(f"No se puede continuar con la actualizacion debido a un problema en el campo {texto_esperado}")

    def test_editar_precio_incorrecto(self):
        try:
            driver = self.driver
            driver.get(f"{self.url_base}/editar/{self.producto_inicial.id}")
            pagina_editar = self.EditarPage
            codigo_producto = "00000012"
            nombre_producto = "Actualizado"
            descripcion_producto = "Actualizado FM"
            cantidad_producto = 1
            precio_producto = 0

            pagina_editar.ingresar_codigo(codigo_producto)
            pagina_editar.ingresar_nombre(nombre_producto)
            pagina_editar.ingresar_descripcion(descripcion_producto)
            pagina_editar.ingresar_cantidad_minima(cantidad_producto)
            pagina_editar.ingresar_precio(precio_producto)
            pagina_editar.editar()

            self.assertNotEqual(self.url_base, driver.current_url)
            texto_esperado = pagina_editar.recuperar_alerta()
            self.assertEqual('', texto_esperado)
        except Exception as e:
            self.fail(f"Unable to continue with the update due to a problem in the field {texto_esperado}")

    @classmethod
    def tearDownClass(cls):
        Producto.objects.all().delete()
        if cls.driver:
            cls.driver.quit()

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(EditarProductoTest))
    return suite

if __name__ == '__main__':
    # Crear un ejecutor de pruebas que ejecuta la suite y genera un reporte en HTML
    runner = HtmlTestRunner.HTMLTestRunner(
        output='reportes',  # Carpeta donde se guardará el reporte
        report_name='problemas_al_actualizar_producto',  # Nombre del archivo del reporte
        report_title='No actualizar productos invalidos usando Selenium',  # Titulo del reporte
        combine_reports=True,  # Combina todas las pruebas en un único reporte
        add_timestamp=True  # Agrega una marca de tiempo al reporte
    )
    # Ejecutar la suite
    runner.run(suite())