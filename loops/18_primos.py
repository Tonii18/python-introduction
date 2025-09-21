def esPrimo(numero):
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    
    return primo

numero = int(input("Introduce un numero entero: "))

if esPrimo(numero):
    print(numero, "es primo.")
else:
    print(numero, "no es primo.")
