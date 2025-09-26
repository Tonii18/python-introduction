import random

def crear_matriz(dimension):
    lista = []

    for i in range(dimension):
        fila = []
        for j in range(dimension):
            numero = random.randint(1, 9)
            fila.append(numero)
        lista.append(fila)
    
    return lista

def mostrar_matriz(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end = ' ')
        print()

def sumar_matrices(arr1, arr2):
    array = []
    for i in range(len(arr1)):
        fila = []
        for j in range(len(arr1[0])):
            fila.append(arr1[i][j] + arr2[i][j])
        array.append(fila)

    return array


dimension = int(input("Introduce la dimension de los arrays: "))

array_1 = crear_matriz(dimension)
array_2 = crear_matriz(dimension)

print('Matriz 1: ')
mostrar_matriz(array_1)

print('Matriz 2: ')
mostrar_matriz(array_2)

nueva = sumar_matrices(array_1, array_2)

print('Suma de las dos matrices: ')

mostrar_matriz(nueva)


