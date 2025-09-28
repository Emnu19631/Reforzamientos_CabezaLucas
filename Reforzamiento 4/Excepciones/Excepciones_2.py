"""
2. Crear una función y dentro la respectiva excepción o excepciones para el
siguiente bloque de código para que tu programa no se bloquee, ya que solo
aceptará datos tipos entero y además imprimir un mensaje al usuario la causa
y/o solución. También debe indicar el índice donde ingresarás este nuevo dato,
si el índice está fuera de rango indicárselo al usuario:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]: No es posible ingresar el dato, índice fuera de rango
- Usarás dos tipos diferentes de excepciones (IndexError TypeError) y
- Usarás la función al menos 3 veces incluyendo un caso de error
"""


lista = [2, 6, 10, 4, 5, 23, 1]

def insertar_dato(lista, indice, valor):
    try:
        if not isinstance(valor, int):
            raise TypeError("El dato debe ser un número entero")

        lista[indice] = valor
        print(f"Dato {valor} insertado correctamente en la posición {indice}")

    except IndexError:
        print(f"No es posible ingresar el dato: índice {indice} fuera de rango")
    except TypeError as e:
        print(f" Error de tipo: {e}. Solución: ingrese un número entero válido.")

insertar_dato(lista, 2, 99)
insertar_dato(lista, 10, 50)
insertar_dato(lista, 3, "hola")

print("Lista final:", lista)
