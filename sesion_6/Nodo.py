class Nodo:
    """
    Representa un Nodo de la lista Encadenada
    """

    elemento = None
    siguiente = None

    def __init__(self, elemento=None, nodo=None):
        self.elemento = elemento
        self.siguiente = nodo