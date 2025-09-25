def es_simetrica(array):
    simetrica = True

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] != array[j][i]:
                simetrica = False

    return simetrica

matriz = [
    [7, 3, 5, 2],
    [3, 4, 6, 1],
    [5, 6, 8, 0],
    [2, 1, 0, 9],
]

print(es_simetrica(matriz))