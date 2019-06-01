from unittest import TestCase
from recursion import suma_elementos


class TestSuma_elementos(TestCase):

    def test_suma_elementos(self):
        # Caso estandar
        dado = [1, 2, 3, 4]
        espero = 10
        real = suma_elementos(dado)
        self.assertEqual(espero, real)

        # Caso extremo
        dado = []
        espero = 0
        real = suma_elementos(dado)
        self.assertEqual(espero, real)


