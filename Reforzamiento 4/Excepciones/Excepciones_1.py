"""1. Crear una función llamada division_segura(a, b) que recibirá dos
números e intentará devolver la división de a entre b
Si b es cero, debe capturar la excepción y mostrar mensaje “Error: no puedes
dividir entre cero”
Si ambos valores son válidos deben imprimir el resultado Independientemente
del resultado, debe imprimir “Operación finalizada” al final
- Usar try, except, finally

- Valida que los datos ingresados sean numéricos de lo contrario mostrar
“Error: Entrada no numérica”
- Usarás la función al menos 3 veces incluyendo un caso de error"""

def division_segura(a, b):
    try:
        resultado = a / b
        print(f"El resultado de {a} / {b} es {resultado}")
    except ZeroDivisionError:
        print("Error: no puedes dividir entre cero")
    except TypeError:
        print("Error: Entrada no numérica")
    finally:
        print("Operación finalizada")
try:
    a1 = float(input("Ingrese el primer número para caso 1: "))
    b1 = float(input("Ingrese el segundo número para caso 1: "))
    division_segura(a1, b1)

    a2 = float(input("Ingrese el primer número para caso 2: "))
    b2 = float(input("Ingrese el segundo número para caso 2: "))
    division_segura(a2, b2)

    a3 = input("Ingrese el primer número para caso 3: ")
    b3 = input("Ingrese el segundo número para caso 3: ")
    a3 = float(a3)
    b3 = float(b3)
    division_segura(a3, b3)

except ValueError:
    print("Error: Entrada no numérica")