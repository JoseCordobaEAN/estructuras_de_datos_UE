class Casa:

    def __init__(self,direccion, n_habitaciones, n_baños = 1):
        self.direccion = direccion
        self.n_habitaciones = n_habitaciones
        self.n_baños = n_baños

    def __repr__(self):
        return f'Casa en {self.direccion} de {self.n_habitaciones}' \
            f' habitaciones y {self.n_baños} baños'


class Patio:

    def __init__(self, metros):
        self.metros = metros

    def __repr__(self):
        return f'un patio de {self.metros} metros cuadrados'