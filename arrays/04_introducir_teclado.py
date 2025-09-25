def get_media(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma // len(lista)


lista = []

mayor = 0
menor = 101
media = 0

mayor_media = 0
menor_media = 0

numero = int(input('Introduce numeros enteros: '))

while numero > 0:
    lista.append(numero)
    if len(lista) == 20:
        print('La longitud de la lista ha llegado a su maximo (20).')
        break
    
    numero = int(input('Introduce numeros enteros: '))

media = get_media(lista)

print('Lista de numeros: ')

for numero in lista:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    
    if numero > media:
        mayor_media += 1
    if numero < media:
        menor_media += 1

    print(numero, end = ' ')

print('\nNumero mas grande: ', mayor)
print('Numero mas pequeño: ', menor)
print('Media: ', media)
print('Numeros que son mayores que la media: ', mayor_media)
print('Numeros que son menores que la media: ', menor_media)