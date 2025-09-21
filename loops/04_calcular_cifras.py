""" Escribir un programa que lea un número entero positivo N y calcule cuántas cifras tiene. """

contador = 0
numero = int(input("Introduce un numero entero: "))
numero_final = numero

while numero > 0:
    numero //= 10
    contador += 1

print("El ", numero_final, "tiene ", contador, " cifras.")