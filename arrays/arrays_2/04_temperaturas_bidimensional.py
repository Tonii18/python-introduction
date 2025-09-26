import random

def rellenar(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            temperatura = random.randint(15, 35)
            array[i][j] = temperatura

def listar(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end = ' ')

def estadistica(array):
    mayor = 0
    menor = 101
    suma = 0
    numero_dias = len(array)
    temperaturas_diarias = len(array[0])

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] > mayor:
                mayor = array[i][j]
            if array[i][j] < menor:
                menor = array[i][j]
            suma += array[i][j]
    
    media = suma // (len(array) * len(array[0]))

    print('Temperatura mas grande: ', mayor)
    print('Temperatura mas pequeña: ', menor)
    print('Temperatura media: ', media)
    print('Numero de dias: ', numero_dias)
    print('Numero de temperaturas por dia: ', temperaturas_diarias)
    


filas = int(input('Introduce el numero de dias:'))
columnas = int(input('Introduce el numero de temperaturas por dia: '))

temperaturas = [[0 for _ in range(columnas)] for _ in range(filas)]

rellenar(temperaturas)
listar(temperaturas)
estadistica(temperaturas)

