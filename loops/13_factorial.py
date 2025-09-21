numero = int(input("Introduce un numero entero: "))

factorial = 1

for i in range(numero, 0, -1):
    factorial *= i
    if i > 1:
        print(i, "x", end = ' ')
    else:
        print(i, " = ", factorial)
