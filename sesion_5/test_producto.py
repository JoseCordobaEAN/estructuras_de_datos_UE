from unittest import TestCase
from recursion2 import producto


class TestProducto(TestCase):
    def test_producto(self):
        # Prueba estandar
        dado_n1 = 5
        dado_n2 = 8
        espero = 40
        realmente = producto(dado_n1, dado_n2)
        self.assertEqual(espero, realmente)

        # Prueba extremo
        dado_n1 = 8
        dado_n2 = 0
        espero = 0
        realmente = producto(dado_n1, dado_n2)
        self.assertEqual(espero, realmente)

        # Prueba estandar
        dado_n1 = -5
        dado_n2 = 8
        espero = -40
        realmente = producto(dado_n1, dado_n2)
        self.assertEqual(espero, realmente)

        # Prueba estandar
        dado_n1 = -5
        dado_n2 = -8
        espero = 40
        realmente = producto(dado_n1, dado_n2)
        self.assertEqual(espero, realmente)

        # Prueba estandar
        dado_n1 = 5
        dado_n2 = -8
        espero = -40
        realmente = producto(dado_n1, dado_n2)
        self.assertEqual(espero, realmente)
