from unittest import TestCase
from recursion import busqueda_binaria


class TestBusqueda_binaria(TestCase):

    def test_busqueda_binaria(self):
        # Probar caso extremo
        lista_dada = [1, 2, 8, 20, 25, 50, 500]
        elemento_dado = 1
        espero = 0
        real = busqueda_binaria(lista_dada, elemento_dado)
        self.assertEqual(espero, real)

        # Probar caso extremo
        lista_dada = [1, 2, 8, 20, 25, 50, 193, 600]
        elemento_dado = 600
        espero = 7
        real = busqueda_binaria(lista_dada, elemento_dado)
        self.assertEqual(espero, real)

        # Probar caso estandar
        lista_dada = [1, 2, 8, 20, 25, 50, 500]
        elemento_dado = 20
        espero = 3
        real = busqueda_binaria(lista_dada, elemento_dado)
        self.assertEqual(espero, real)

        # Probar caso estandar
        lista_dada = [3, 7, 8, 9, 11, 21, 27]
        elemento_dado = 21
        espero = 5
        real = busqueda_binaria(lista_dada, elemento_dado)
        self.assertEqual(espero, real)

        # Probar caso excepcional
        lista_dada = [1, 2, 8, 20, 25, 50, 500]
        elemento_dado = -50
        espero = ValueError
        self.assertRaises(espero, busqueda_binaria, lista_dada, elemento_dado)
