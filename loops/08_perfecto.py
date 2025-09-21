def sumaDivisores(numero):
    suma = 0
    for i in range(1, numero - 1):
        if numero % i == 0:
            suma += i
    return suma


numero = int(input("Introduce un numero entero: "))

if numero == sumaDivisores(numero):
    print("Es un numero perfecto")
else:
    print("No es un numero perfecto")
