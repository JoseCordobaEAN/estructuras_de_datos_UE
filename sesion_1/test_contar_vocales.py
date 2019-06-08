from unittest import TestCase
from funciones import contar_vocales

class TestContar_vocales(TestCase):
    def test_contar_vocales(self):

        dado = 'hola mundo'
        espero = 4
        realmente = contar_vocales(dado)
        print(f'contando vocales en {dado}, esperamos {espero}')
        self.assertEqual(espero, realmente)

        dado = 'qwqwrtpppñlk'
        espero = 0
        realmente = contar_vocales(dado)
        print(f'contando vocales en {dado}, esperamos {espero}')
        self.assertEqual(espero, realmente)

        dado = '!"$#"!"!$"%'
        espero = 0
        realmente = contar_vocales(dado)
        print(f'contando vocales en {dado}, esperamos {espero}')
        self.assertEqual(espero, realmente)

        dado = ''
        espero = 0
        realmente = contar_vocales(dado)
        print(f'contando vocales en {dado}, esperamos {espero}')
        self.assertEqual(espero, realmente)

        dado = 'aeiiioiiooiaaeuu'
        espero = 16
        realmente = contar_vocales(dado)
        print(f'contando vocales en {dado}, esperamos {espero}')
        self.assertEqual(espero, realmente)
