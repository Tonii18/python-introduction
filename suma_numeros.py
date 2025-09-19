suma = 0
numero = int(input("Introduce un numero: "))

for i in range(numero, numero + 100):
    print(i, end= ' ')
    suma += i

print("Suma: ", suma)