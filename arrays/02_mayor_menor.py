import random

lista = []

mayor = 0
menor = 101

print('Lista: ')

for i in range(10):
    numero = random.randint(1, 100)
    lista.append(numero)
    print(numero, end = ' ')

for numero in lista:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print('\nNumero mayor: ', mayor)
print('Numero menor: ', menor)