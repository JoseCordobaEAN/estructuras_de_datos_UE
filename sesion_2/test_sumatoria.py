from unittest import TestCase
from sumatoria import *
from datetime import datetime

class TestSumatoria(TestCase):


    def test_sumatoria(self):
        """
        Prueba una sumatoria

        :return: none
        """
        ahora = datetime.now()
        print(f'El algoritmo empezó {ahora}')
        dado = 100000000
        espero = 5000000050000000
        realmente = sumatoria(dado)
        despues = datetime.now()
        duracion = despues - ahora
        print(f'el algoritmo terminó {despues} la duración fue de {duracion}')
        self.assertEqual(espero, realmente)


    # def test_sumatoria(self):
    #     ahora = datetime.now()
    #     print(f'El algoritmo empezó {ahora}')
    #     dado = 100000000
    #     espero = 5000000050000000
    #     realmente = sumatoria_v2(dado)
    #     despues = datetime.now()
    #     print(f'el algoritmo terminó {despues}')
    #     self.assertEquals(espero, realmente)
