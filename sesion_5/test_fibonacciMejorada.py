from unittest import TestCase
from recursion2 import fibonacciMejorada


class TestFibonacciMejorada(TestCase):
    def test_fibonacciMejorada(self):
        # Probamos un caso estandar
        dado = 8
        espero = 21
        real = fibonacciMejorada(dado)
        self.assertEqual(espero, real)

        # Probamos un caso estandar
        dado = 4
        espero = 3
        real = fibonacciMejorada(dado)
        self.assertEqual(espero, real)

        # Probamos un caso Excepcional
        dado = -1
        espero = ValueError
        self.assertRaises(espero, fibonacciMejorada, dado)

        # Probamos un caso estandar
        dado = 975
        espero = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
        real = fibonacciMejorada(dado)
        self.assertEqual(espero, real)
