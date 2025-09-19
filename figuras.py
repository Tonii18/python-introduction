def triangulo():
    for i in range(10):
        for j in range(i - 1):
            print("*", end = ' ')
        print()

def cuadrado():
    for i in range(10):
        for j in range(10):
            print("*", end = ' ')
        print()


shape = input("Introduce el tipo de figura que quieres dibujar: ")
if shape == 'triangulo':
    triangulo();
elif shape == 'cuadrado':
    cuadrado();
else:
    print("Opcion no valida")