matriz = [
    [7, 3, 5],
    [3, 4, 6],
    [5, 6, 8],
]

suma_filas = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        suma_filas += matriz[i][0]
        matriz.append(suma_filas)
        print(matriz[i][j], end = ' ')
    suma_filas = 0
    print()
