from unittest import TestCase
from funciones import es_vocal


class TestEs_vocal(TestCase):

    def test_es_vocal(self):
        dado = 'O'
        espero = True
        realmente = es_vocal(dado)
        print(f'validando es vocal con el parametro {dado}')
        self.assertEquals(espero, realmente)

        dado = 'Y'
        espero = False
        realmente = es_vocal(dado)
        print(f'validando es vocal con el parametro {dado}')
        self.assertEquals(espero, realmente)

        dado = 'io'
        espero = False
        realmente = es_vocal(dado)
        print(f'validando es vocal con el parametro {dado}')
        self.assertEquals(espero, realmente)
