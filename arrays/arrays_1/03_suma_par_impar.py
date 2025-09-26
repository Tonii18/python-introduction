import random

lista = []

for i in range(10):
    numero = random.randint(1, 100)
    lista.append(numero)
    print(numero, end = ' ')

sumaPar = 0
sumaImpar = 0

for i in range(len(lista)):
    if i % 2 == 0:
        sumaPar += lista[i]
    elif i % 2 != 0:
        sumaImpar += lista[i]

print('\nSuma de los indices par: ', sumaPar)
print('Suma de los indices impar: ', sumaImpar)
