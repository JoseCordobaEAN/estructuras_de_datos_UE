from unittest import TestCase
from sumatoria import sumatoria
from datetime import datetime

class TestSumatoria(TestCase):


    def test_sumatoria(self):
        ahora = datetime.now()
        print(f'El algoritmo empezó {ahora}')
        dado = 100000000
        espero = 5000000050000000
        realmente = sumatoria(dado)
        despues = datetime.now()
        print(f'el algoritmo terminó {despues}')
        self.assertEquals(espero, realmente)
