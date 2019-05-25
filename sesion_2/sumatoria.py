def sumatoria(num):
    acumulador = 0
    for i in range(num + 1):
        acumulador += i
    return acumulador


def sumatoria_v2(num):
    return num * (num + 1) // 2