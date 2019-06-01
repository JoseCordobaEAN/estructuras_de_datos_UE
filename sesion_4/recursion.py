def factorial(num):
    """
    (int) -> int

    Calcula el factorial de un número entero

    >>> factorial(3)
    6
    >>> factorial(4)
    24

    :param num: int el numero a evaluar
    :return: int el resultado del factorial
    """
    if num == 1 or num == 0:
        return 1
    elif num < 0:
        raise ValueError(f'no existe el factorial '
                         f'para {num}')
    return num * factorial(num - 1)


def busqueda_binaria(lista, elemento):
    """
    (list, elem) -> int

    Retorna la poscicion en una lista ordenada del elemento dado

    >>> busqueda_binaria([1, 2, 3], 2)
    1
    >>> busqueda_binaria([8, 50, 90, 100], 100)
    3

    :param lista: la lista ordenada para buscar
    :param elemento: el elemento buscado
    :return: int, la poscicion en la lista del elemento
    """
    mitad = len(lista) // 2
    if not lista:
        raise ValueError(f'{elemento} no está en la lista')
    elif elemento == lista[mitad]:
        return mitad
    elif elemento < lista[mitad]:
        return busqueda_binaria(lista[:mitad], elemento)
    elif elemento > lista[mitad] and len(lista) == 1:
        raise ValueError(f'{elemento} no está en la lista')
    return mitad + busqueda_binaria(lista[mitad:], elemento)


def suma_elementos(lista):
    """
    Suma todos los elementos de una lista

    >>> suma_elementos([1, 20, 11])
    32

    :param lista:
    :return:
    """
    if len(lista) == 0:
        return 0
    return lista[0] + suma_elementos(lista[1:])
