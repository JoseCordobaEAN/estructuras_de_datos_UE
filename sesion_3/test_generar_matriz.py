from unittest import TestCase
from ejercicios import generar_matriz
from datetime import datetime


class TestGenerar_matriz(TestCase):

    def test_generar_matriz(self):
        ahora = datetime.now()
        print(f'El algoritmo empezó {ahora}')


        dado = [1000, 1000]
        espero_filas = dado[0]
        espero_columnas = dado[1]
        resultado = generar_matriz(dado[0], dado[1])
        resultado_filas = len(resultado)
        resultado_columnas = len(resultado[0])

        despues = datetime.now()
        duracion = despues - ahora
        print(f'el algoritmo terminó {despues} la duración fue de {duracion}')

        self.assertEqual(resultado_filas, espero_filas)
        self.assertEqual(resultado_columnas, espero_columnas)