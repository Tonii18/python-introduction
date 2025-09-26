import random

lista = ['Juan', 'Tifani', 'Andrea', 'Julian', 'Norma', 'Adrian']

def dame_nombre():
    indice = random.randint(0,len(lista)-1)
    return lista[indice]

print(dame_nombre())