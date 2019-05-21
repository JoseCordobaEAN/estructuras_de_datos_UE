def cuadrado(num):
    """
    (num) -> num

    Calcula el cuadrado del numero

    >>> cuadrado(2)
    4
    >>> cuadrado(-2)
    4
    >>> cuadrado(0)
    0

    :param num: int or float el numero a elevar al cuadrado
    :return: num el resultado de elevar num al cuadrado
    """
    return num ** 2


def pitagoras(cateto_opuesto, cateto_adyacente):
    return (cuadrado(cateto_opuesto) + cuadrado(cateto_adyacente)) ** 0.5


def es_vocal(letra):
    """
    (str of len == 1) bool

    Determina si una letra es vocal

    >>> es_vocal('a')
    True
    >>> es_vocal('x')
    False

    :param letra: str of len 1 representa un caracter
    :return: True si es vocal False de lo contrario
    """
    return 1 == len(letra) and letra in 'aeiouAEIOU'


def contar_vocales(frase):
    pass
