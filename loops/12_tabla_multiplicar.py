numero = int(input("Introduce un numero: "))

while numero < 1 or numero > 10:
    numero = int(input("El numero debe comprender entre el 1 y el 10: "))

for i in range (1, 10 + 1):
    print(numero, " X ", i, " = ", numero*i)