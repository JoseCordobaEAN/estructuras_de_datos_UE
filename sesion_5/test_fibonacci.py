from unittest import TestCase
from recursion2 import fibonacci

class TestFibonacci(TestCase):

    def test_fibonacci(self):
        # Probamos un caso estandar
        dado = 8
        espero = 21
        real = fibonacci(dado)
        self.assertEqual(espero, real)

        # Probamos un caso estandar
        dado = 4
        espero = 3
        real = fibonacci(dado)
        self.assertEqual(espero, real)


        # Probamos un caso Excepcional
        dado = -1
        espero = ValueError
        self.assertRaises(espero, fibonacci, dado)

        # Probamos un caso estandar
        dado = 100
        espero = 3
        real = fibonacci(dado)
        self.assertEqual(espero, real)
