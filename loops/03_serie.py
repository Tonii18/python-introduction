termino = int(input("Introduce el n termino de la serie: "))

suma = 0
for i in range(1, termino + 1):
    suma += 1 / i

print(f"Suma: ", suma)