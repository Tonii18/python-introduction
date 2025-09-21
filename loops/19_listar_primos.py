def esPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Introduce un numero entero: "))

for i in range(numero):
    if esPrimo(i):
        print(i)

