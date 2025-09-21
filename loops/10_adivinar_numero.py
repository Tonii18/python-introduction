import random
import time

contador = 1

print("Generando numero...")
time.sleep(2.00)
generado = random.randint(0, 100)
print("Numero generado!")

numero = int(input("Intenta adivinar el numero: "))

while numero != generado:
    print("Numero incorrecto.")
    if numero > generado:
        print("El numero generado es mas pequeño")
    elif numero < generado:
        print("El numero generado es mas grande")
    
    contador += 1
    
    numero = int(input("Vuelve a intentarlo: "))

print("Enhorabuena! Has acertado el numero en ", contador, " intentos.")