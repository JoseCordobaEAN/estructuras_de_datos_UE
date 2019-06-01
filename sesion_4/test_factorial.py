from unittest import TestCase
from recursion import *

class TestFactorial(TestCase):

    def test_factorial(self):
        # Mira un caso normal
        dado = 5
        espero = 120
        real = factorial(dado)
        self.assertEqual(espero, real)

        # Valida un caso extremo
        dado = 0
        espero = 1
        real = factorial(dado)
        self.assertEqual(espero, real)

        # Valida un caso exepcional
        dado = -1
        espero = ValueError
        self.assertRaises(espero, factorial, dado)