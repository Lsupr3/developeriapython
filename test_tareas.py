import unittest
from tareas import agregar, borrar, imprime_tareas
from unittest.mock import patch

class Test_tareas(unittest.TestCase):
    def test_si_agrego_nueva_tarea_len_de_tareas_crece_en_uno(self):
        tareas=[]
        tarea={
            "Titulo": "Pepe",
            "Descripcion": "Oriol",
            "Prioridad": "Media",
            "Estado": "Nueva"}
        resultado = agregar(tareas, tarea, True)
        print(tareas)
        self.assertGreater(len(resultado), 0, f"El resultado es: {resultado} y el esperado es mayor de 0" )

    def test_si_borro_una_tarea_len_de_tareas_igual_0(self):
        tareas=[]
        tarea={
            "Titulo": "Pepe",
            "Descripcion": "Oriol",
            "Prioridad": "Media",
            "Estado": "Nueva"}
        agregar(tareas, tarea, True)
        resultado=borrar(tareas, titulo="Pepe", IsTest=True)
        print(tareas)
        self.assertEqual(len(resultado), 0, f"El resultado es: {resultado} y el esperado es mayor de 0" )

    def test_si_agrego_una_tarea_e_imprimo_el_resultado_es_de_len0(self):
        tareas=[]
        tarea={
            "Titulo": "Pepe",
            "Descripcion": "Oriol",
            "Prioridad": "Media",
            "Estado": "Nueva"}
        agregar(tareas, tarea, True)
        resultado=imprime_tareas(tareas)
        self.assertGreater(len(resultado), 0, f"El resultado es: {resultado} y el esperado es mayor de 0" )

    def test_si_no_hay_tarea_en_tareas_e_imprimo_el_resultado_es_mensaje_de_texto(self):
        tareas=[]
        resultado=imprime_tareas(tareas)
        self.assertEqual(resultado, "No hay ninguna tarea pendiente", f"El resultado es: {resultado} y el esperado es mayor de 0" )


if __name__ == '__main__':
    unittest.main()