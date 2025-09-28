"""
5. Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados por el
usuario también y un segundo parámetro que eliminará de la lista que fue
ingresada a la función, finalmente el output de la función será la lista
actualizada sin el valor que se sacará de la lista. Mostrar también la lista
original y el número que fue eliminado.
"""

def eliminar_valor(lista, valor):
    lista_actualizada = lista.copy()
    if valor in lista_actualizada:
        lista_actualizada.remove(valor)
        print(f"Número eliminado: {valor}")
    else:
        print(f"El número {valor} no está en la lista")
    return lista_actualizada

try:
    n = int(input("Ingrese la cantidad de números para la lista: "))
    if n <= 0:
        print("Error: La cantidad debe ser mayor que 0.")
        exit()
except ValueError:
    print("Error: Ingrese un número entero válido.")
    exit()

lista_original = []
for i in range(n):
    try:
        numero = float(input(f"Ingrese el número {i+1}: "))
        lista_original.append(numero)
    except ValueError:
        print("Error: Ingrese un número válido.")
        exit()

try:
    valor_eliminar = float(input("Ingrese el número a eliminar de la lista: "))
except ValueError:
    print("Error: Ingrese un número válido.")
    exit()

print(f"Lista original: {lista_original}")

lista_resultante = eliminar_valor(lista_original, valor_eliminar)
print(f"Lista actualizada: {lista_resultante}")