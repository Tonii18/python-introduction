import random

lista = []

print('Lista ordenada: ')

for i in range(10):
    numero = random.randint(1, 100)
    lista.append(numero)
    print(numero, end = ' ')

print('\nLista a la inversa: ')

for i in range(9, -1, -1):
    print(lista[i], end = ' ')