"""
2. Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la función una
vez y mostrar el resultado por consola). Los números serán ingresados y
solicitados al usuario.
"""
def cuadrados_entre_numeros(inicio, fin):
    """Muestra los cuadrados de los números enteros entre inicio y fin (inclusive)."""
    for num in range(inicio, fin + 1):
        print(f"El cuadrado de {num} es {num ** 2}")

try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
except ValueError:
    print("Error: Ingrese números enteros válidos.")
    exit()

inicio = min(num1, num2)
fin = max(num1, num2)

cuadrados_entre_numeros(inicio, fin)