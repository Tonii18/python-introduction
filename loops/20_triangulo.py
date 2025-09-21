tamaño = int(input("Introduce el tamaño del triangulo: "))

for i in range(tamaño):
    for j in range(tamaño,i,-1):
        print("*", end = ' ')
    print()