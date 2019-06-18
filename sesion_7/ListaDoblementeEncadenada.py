from sesion_6 import ListaAbstracta as la
from sesion_7 import NodoDoble as nd


class ListaDoblementeEncadena(la):

    size = 0
    cabeza = None
    cola = None

    def es_vacia(self):
        return self.size == 0

    def primero(self):
        if not self.es_vacia():
            return self.cabeza.elemento

    def ultimo(self):
        if not self.es_vacia():
            return self.cola.elemento

    def buscar(self, elemento_buscado):
        pass

    def agregar_al_inicio(self, elemento):
        nuevo = nd(elemento, self.cabeza)
        self.cabeza = nuevo
        self.size += 1
        if self.size == 1:
            self.cola = nuevo

    def agregar_al_final(self, elemento):
        nuevo = nd(elemento, None, self.cola)
        self.cola = nuevo
        self.size += 1
        if self.size == 1:
            self.cabeza = nuevo

    def remover_primero(self):
        if self.size == 1:
            self.cabeza = None
            self.cola = None
        elif self.size > 1:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        elif self < 1:
            raise ValueError('No se puede remover en una lista vacía')
        self.size -= 1


    def remover_ultimo(self):
        if self.size == 1:
            self.cabeza = None
            self.cola = None
        elif self.size > 1:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        elif self < 1:
            raise ValueError('No se puede remover en una lista vacía')
        self.size -= 1