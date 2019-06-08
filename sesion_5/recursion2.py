def fibonacci(n):
    if 2 == n or n == 1:
        return 1
    elif n == 0:
        return 0
    elif n < 1:
        raise ValueError(f'{n} es menor que 1')
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacciMejorada(num):

    # Probamos los casos extremos
    if num == 0:
        return 0
    elif num <0:
        raise ValueError(f'{num} es menor que 1')

    def fib(n):
        if n == 1 or n == 2:
            return [1, 0]
        temp = fib(n-1)
        return [temp[0] + temp[1], temp[0]]

    return fib(num +1 )[0]


def producto(num1, num2):
    if num2 == 0:
        return 0
    elif num1 < 0 and num2 < 0:
        return producto(-num1, -num2)
    elif num2 < 0:
        return producto(num2, num1)
    return num1 + producto(num1, num2 - 1)

