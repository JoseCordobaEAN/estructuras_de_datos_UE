from enum import Enum

class ListaAbstracta(Enum):

    size = 0

    def es_vacia(self):
        pass

    def primero(self):
        pass

    def ultimo(self):
        pass

    def buscar(self, elemento_buscado):
        pass

    def agregar_al_inicio(self, elemento):
        pass

    def agregar_al_final(self, elemento):
        pass

    def remover_primero(self):
        pass

    def remover_ultimo(self):
        pass