"""1. Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los números
cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, según
sea conveniente."""

def suma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

while True:
    try:
        num1 = int(input("Ingrese el primer número positivo: "))
        num2 = int(input("Ingrese el segundo número positivo: "))
        if num1 > 0 and num2 > 0:
            break
        else:
            print("Error: Los números deben ser positivos.")
    except ValueError:
        print("Error: Ingrese números enteros válidos.")

suma1 = suma_digitos(num1)
suma2 = suma_digitos(num2)

if suma1 > suma2:
    mayor = num1
elif suma2 > suma1:
    mayor = num2
else:
    mayor = f"Ambos ({num1} y {num2}, suma: {suma1})"

menores_10 = []
if suma1 < 10:
    menores_10.append(f"{num1} (suma: {suma1})")
if suma2 < 10:
    menores_10.append(f"{num2} (suma: {suma2})")

print(f"\nNúmero con mayor suma de dígitos: {mayor}")
if menores_10:
    print("Números con suma de dígitos menor a 10:", ", ".join(menores_10))
else:
    print("No hay números con suma de dígitos menor a 10.")