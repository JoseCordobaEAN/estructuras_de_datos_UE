from random import randint


def generar_matriz(n, m):
    """
    Genera una mtriz aleatoria

    :param n: el numero de filas de la matriz
    :param m: el numero de columnas de la matriz
    :return: una matriz de enteros n x m
    """
    resultado = []
    for fila in range (n):
        vector = []
        for columna in range(m):
            vector.append(randint(0,9))
        resultado.append(vector)
    return resultado