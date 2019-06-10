from ListaAbstracta import ListaAbstracta

class ListaEncadenada(ListaAbstracta):

    class Nodo:

        elemento = None
        siguiente = None

        def __init__(self, elemento = None, nodo = None):
            self.elemento = elemento
            self.siguiente = nodo


    def es_vacia(self):
        super().es_vacia()

    def primero(self):
        super().primero()

    def ultimo(self):
        super().ultimo()

    def buscar(self, elemento_buscado):
        super().buscar(elemento_buscado)

    def agregar_al_inicio(self, elemento):
        super().agregar_al_inicio(elemento)

    def agregar_al_final(self, elemento):
        super().agregar_al_final(elemento)

    def remover_primero(self):
        super().remover_primero()

    def remover_ultimo(self):
        super().remover_ultimo()