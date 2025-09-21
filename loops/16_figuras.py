filas = int(input("Introduce el numero de filas: "))
columnas = int(input("Introduce el numero de columnas: "))

if filas > 10 or columnas > 10:
    filas = 10
    columnas = 10

for i in range(filas):
    for j in range(columnas):
        print("*", end = ' ')
    print()