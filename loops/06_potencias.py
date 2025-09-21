x = int(input("Introduce la base: "))
n = int(input("Introduce el exponente: "))

for i in range(1, n):
    x += x

print(f"Resultado: ", x)