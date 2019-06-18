from ListaAbstracta import ListaAbstracta
from Nodo import Nodo

class ListaEncadenada(ListaAbstracta):

    def __init__(self):
        """
        Crea una nueva lista
        """
        self.cabeza = None
        self.size = 0
        self.cola = None

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
        return self.cola.elemento

    def buscar(self, elemento_buscado):
        copia = self.cabeza
        for i in range(self.size):
            if elemento_buscado == copia.elemento:
                return i
        return -1

    def agregar_al_inicio(self, elemento):
        nodo_auxiliar = Nodo()
        nodo_auxiliar.elemento = elemento
        nodo_auxiliar.siguiente = self.cabeza
        self.cabeza = nodo_auxiliar
        self.size += 1


    def agregar_al_final(self, elemento):
        nuevo = Nodo(elemento)
        if self.size == 0:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.size += 1

    def remover_primero(self):
        if not self.es_vacia():
            nuevo = self.cabeza.siguiente
            self.cabeza = nuevo
            if self.size == 1:
                self.cola = nuevo
            self.size -=1



    def remover_ultimo(self):
        auxiliar = self.cabeza
        penultimo = None
        while auxiliar:
            penultimo = auxiliar
            auxiliar = auxiliar.siguiente
        if self.size > 0:
            penultimo.siguiente = None
            self.size -= 1
        self.cola == penultimo