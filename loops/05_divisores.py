def obtenerDivisores(numero):
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)

numero = int(input("Introduce un numero entero: "))
print("DIVISORES DEL ", numero, ": ")
obtenerDivisores(numero)
