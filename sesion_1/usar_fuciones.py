from funciones import *

numero = 81
print(f'{numero} al cuadrado es {cuadrado(numero)}')


cateto_1 , cateto_2 = [3, 3]
hipo = pitagoras(cateto_1, cateto_2)

print(f'la hipotenusa para el triengulo con catetos {cateto_1} y {cateto_2} es {hipo}')
