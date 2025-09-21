def obtenerSuma(num1, num2):
    sumaPar = 0
    sumaImpar = 0
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            sumaPar += i
        else:
            sumaImpar += i
    
    print("Suma de los pares: ", sumaPar)
    print("Suma de los impares: ", sumaImpar)


a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))

while a > b:
    print("El valor de A debe ser menor que el de B, vuelve a introducir valores")
    a = int(input("Introduce el primer numero: "))
    b = int(input("Introduce el segundo numero: "))

obtenerSuma(a, b)