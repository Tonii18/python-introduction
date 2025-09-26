lista = []

cantidad = int(input("¿Cuantos numeros quieres introducir?: "))

for i in range(cantidad):
    numero = int(input("Introduce un numero entero: "))
    lista.append(numero)

print('Lista ordenada: ', lista)
lista.reverse()
print('Lista inversa: ', lista)