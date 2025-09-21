numero = int(input("Introduce un numero entero entre el 1 y el 10: "))

while numero < 1 or numero > 10:
    numero = int(input("El numero debe estar comprendido entre 1 y 10, intentalo de nuevo: "))


print("Tabla del ", numero)
print("------------------")

for i in range(1, 11):
    print(numero, " x ", i, " = ", numero * i)

numero = int(input("Introduce otro numero: "))