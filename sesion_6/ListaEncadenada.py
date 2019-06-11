from ListaAbstracta import ListaAbstracta
from Nodo import Nodo

class ListaEncadenada(ListaAbstracta):

    def __init__(self):
        """
        Crea una nueva lista
        """
        self.cabeza = None
        self.size = 0

    def es_vacia(self):
        """
        Decide si la lista es vacía
        :return: True si la lista es vacía, False de lo contrario
        """
        return self.size == 0

    def primero(self):
        """
        Retorna el primer elemento de la lista
        :return:
        """
        return self.cabeza.elemento

    def ultimo(self):
        super().ultimo()

    def buscar(self, elemento_buscado):
        super().buscar(elemento_buscado)

    def agregar_al_inicio(self, elemento):
        nodo_auxiliar = Nodo()
        nodo_auxiliar.elemento = elemento
        nodo_auxiliar.siguiente = self.cabeza
        self.cabeza = nodo_auxiliar
        self.size += 1


    def agregar_al_final(self, elemento):
        super().agregar_al_final(elemento)

    def remover_primero(self):
        super().remover_primero()

    def remover_ultimo(self):
        super().remover_ultimo()