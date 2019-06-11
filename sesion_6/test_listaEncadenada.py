from unittest import TestCase
from ListaEncadenada import ListaEncadenada


class TestListaEncadenada(TestCase):


    def test_es_vacia(self):
        dado = ListaEncadenada()
        espero = True
        realmente = dado.es_vacia()
        self.assertEqual(espero, realmente)


    def test_primero(self):
        dado = ListaEncadenada()
        dato = "Hola primero"
        dado.agregar_al_inicio(dato)
        espero = dado.primero()
        self.assertEqual(espero, dato)

    def test_ultimo(self):
        self.fail()

    def test_buscar(self):
        self.fail()

    def test_agregar_al_inicio(self):
        dado = ListaEncadenada()
        dato = "Hola mundo"
        dado.agregar_al_inicio(dato)
        espero = dado.primero()
        self.assertEqual(espero, dato)
        self.assertEqual(dado.size, 1)

    def test_agregar_al_final(self):
        self.fail()

    def test_remover_primero(self):
        self.fail()

    def test_remover_ultimo(self):
        self.fail()
