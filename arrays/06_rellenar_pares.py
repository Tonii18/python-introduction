import random

def rellenar_pares(longitud, fin):
    lista = []

    for i in range(longitud):
        numero = random.randint(2, fin)
        while numero % 2 != 0:
            numero = random.randint(2, fin)
        lista.append(numero)

    return lista

lista = rellenar_pares(10, 20)
print(lista)