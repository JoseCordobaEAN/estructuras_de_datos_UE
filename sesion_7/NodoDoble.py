class NodoDoble:

    elemento = None
    anterior = None
    siguiente = None

    def __init__(self,
                 elemento = None,
                 siguiente = None,
                 anterior = None):
        self.elemento = elemento
        self.anterior = anterior
        self.siguiente = siguiente