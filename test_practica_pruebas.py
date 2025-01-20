import unittest
from practica_pruebas import is_done, is_exist

class Test_practica_pruebas(unittest.TestCase):
    
    def test_el_fichero_no_existe_devuelve_false(self):
        assert is_exist("noexiste.txt") is False
    
    def test_el_fichero_existe_devuelve_true(self):
        assert is_exist("archivo.txt") is True

    def test_si_contiene_la_palabra_prueba_devuelve_true(self):
        assert is_done("archivo.txt", "prueba") is True

    def test_si_contiene_la_palabra_correcto_devuelve_true(self):
        palabraABuscar = "correcta"
        assert is_done("archivo.txt", palabraABuscar) is True

    def test_si_no_contiene_la_palabra_que_envio_por_parametro_devuelve_false(self):
        palabraABuscar = "xxxxxxxxxx"
        assert is_done("archivo.txt", palabraABuscar) is False
    
    def test_si_no_contiene_la_palabraABuscar_y_contiene_la_palabra_no_devuelve_false(self):
        resultado = is_done("archivo.txt")
        self.assertEqual(resultado, False, f"El resultado es: {resultado} y el esperado es: False" )

    def test_si_no_contiene_la_palabraABuscar_y_no_contiene_la_palabra_no_devuelve_false(self):
        resultado = is_done("archivo.txt")
        self.assertEqual(resultado, False, f"El resultado es: {resultado} y el esperado es: False" )



if __name__ == '__main__':
    unittest.main()