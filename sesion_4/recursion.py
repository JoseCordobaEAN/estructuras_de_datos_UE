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