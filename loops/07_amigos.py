def sumaDivisores(numero):
    suma = 0
    for i in range(1, numero - 1):
        if numero % i == 0:
            suma += i
    return suma


num1 = int(input("Introduce el numero 1: "))
num2 = int(input("Introduce el numero 2: "))

suma1 = sumaDivisores(num1)
suma2 = sumaDivisores(num2)

if suma1 == num2 and suma2 == num1:
    print(num1, " y ", num2, " son amigos")
else:
    print(num1, " y ", num2, " no son amigos")

